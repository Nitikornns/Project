<template>
  <v-app>
    <Navbar></Navbar>
    <validation-observer
      class="container d-flex card text-center"
      ref="observer"
    >
      <h2 style="text-align: center">บันทึกข้อมูล</h2>
      <h6 class="message">{{ messagecreate }}</h6>
      <v-form>
        <v-container>
          <validation-provider
            v-slot="{ errors }"
            name="ชื่อจริง"
            rules="required|max:100"
          >
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ชื่อ</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="info.name"
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
                  v-model="info.surname"
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
            name="อีเมล"
            rules="required|email"
          >
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>อีเมล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="info.email"
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
                  v-model="info.telphoneNumber"
                  outlined
                  dense
                  required
                  :error-messages="errors"
                  :counter="10"
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ที่อยู่</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field
                v-model="info.address"
                outlined
                dense
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
        <v-btn
          @click="submitForm"
          depressed
          color="primary"
          class="buttononleft"
          dark
          >บันทึก</v-btn
        ><v-btn
          @click="gotoPreviuosPage"
          color="primary"
          depressed
          class="buttonleft"
          >ย้อนกลับ</v-btn
        >
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
    return { info: {}, infos: [], accountid: {}, messagecreate: "" };
  },
  created() {
    setInterval(this.getCreateMessage, 5000);
  },
  methods: {
    submitForm() {
      this.createInfo();
    },
    getCreateMessage() {
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "บันทึกไม่สำเร็จเกิดข้อผิดพลาด ลองใหม่อีกครั้ง";
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
    async createInfo() {
      await this.getAccountid();
      axiosBase
        .post(
          "/api/infos/",
          {
            accountid: this.accountid,
            name: this.info.name,
            surname: this.info.surname,
            email: this.info.email,
            telphoneNumber: this.info.telphoneNumber,
            address: this.info.address,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.gotoPreviuosPage();
        })
        .catch((err) => {
          console.log(err);
          this.getFailCreateMessage();
        });
    },
    gotoPreviuosPage() {
      this.$router.push({ name: "Dashboard" });
    },
  },
};
</script>
<style src="../src/assets/styles/styles.css" scoped></style>
