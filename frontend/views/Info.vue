<template>
  <v-app id="app">
    <Navbar></Navbar>
    <validation-observer class="container d-flex card" ref="observer">
      <h2 style="text-align: center">บันทึกข้อมูล</h2>
      <v-form>
        <v-container>
          <validation-provider
            v-slot="{ errors }"
            name="ชั้นปี"
            rules="required"
          >
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ชั้นปี</v-subheader> </v-col>
              <v-col cols="7">
                <v-select
                  v-model="student.year"
                  :items="yearsitem"
                  dense
                  outlined
                  :error-messages="errors"
                  required
                ></v-select>
              </v-col>
            </v-row>
          </validation-provider>
          <validation-provider
            v-slot="{ errors }"
            name="ชื่อจริง"
            rules="required|max:100"
          >
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ชื่อ</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.name"
                  :error-messages="errors"
                  required
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
          <validation-provider
            v-slot="{ errors }"
            name="นามสกุล"
            rules="required|max:100"
          >
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>นามสกุล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.surname"
                  outlined
                  dense
                  :error-messages="errors"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
          <validation-provider
            v-slot="{ errors }"
            name="เลขบัตรประชาชน"
            :rules="{ required: true, max: 13, digits: 13 }"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>เลขบัตรประชาชน</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.idcard"
                  outlined
                  dense
                  required
                  :error-messages="errors"
                  :counter="13"
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
          <validation-provider
            v-slot="{ errors }"
            name="อีเมล"
            rules="required|email"
          >
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>อีเมล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.email"
                  outlined
                  dense
                  :error-messages="errors"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
          <validation-provider
            v-slot="{ errors }"
            name="เบอร์โทรศัพท์"
            :rules="{ required: true, max: 10, digits: 10, regex: '0' }"
            ><v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>เบอร์โทรศัพท์</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.telphoneNumber"
                  outlined
                  dense
                  required
                  :error-messages="errors"
                  :counter="10"
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
        </v-container>
        <v-btn @click="submitForm" depressed color="primary" dark>บันทึก</v-btn>
      </v-form>
    </validation-observer>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import jwt_decode from "jwt-decode";
import { axiosBase, getAPI } from "../axios-api";
import { mapState } from "vuex";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Info",
  computed: { ...mapState(["APIData"]) },
  components: { ValidationProvider, ValidationObserver, Navbar },
  data() {
    return {
      student: {},
      yearsitem: ["1", "2", "3", "4"],
      accountid: {},
      messageedit: "",
    };
  },
  methods: {
    submitForm() {
      this.createStudent();
    },
    async getAccountid() {
      let token = localStorage.getItem("access_token");
      let decoded = jwt_decode(token);
      await getAPI
        .get("/accounts/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.accountid = decoded.user_id;
          return this.accountid;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async createStudent() {
      await this.getAccountid();
      axiosBase
        .post(
          "/api/students/",
          {
            accountid: this.accountid,
            year: this.student.year,
            name: this.student.name,
            surname: this.student.surname,
            idcard: this.student.idcard,
            email: this.student.email,
            telphoneNumber: this.student.telphoneNumber,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.$router.push({ name: "Skill" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
