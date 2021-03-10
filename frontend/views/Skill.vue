<template>
  <v-app>
    <Navbar></Navbar>
    <v-card class="container">
      <v-data-table
        :headers="headersskill"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr v-for="skill in skills" :key="skill.skillid">
              <td>{{ skill.name }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <hr />
      <validation-observer
        class="container d-flex card text-center"
        ref="observer"
      >
        <h2 style="text-align: center">{{ title }}</h2>
        <v-card-text>
          <h6 class="message">{{ messagecreate }}</h6>
          <v-form>
            <validation-provider
              v-slot="{ errors }"
              name="ทักษะด้าน"
              rules="required|max:100"
            >
              <v-row align="center" justify="center">
                <v-col cols="3"> <v-subheader>ทักษะด้าน</v-subheader> </v-col>
                <v-col cols="7">
                  <v-text-field
                    v-model="skill.name"
                    :error-messages="errors"
                    required
                    outlined
                    dense
                  ></v-text-field>
                </v-col>
              </v-row>
            </validation-provider>
            <br />
            <v-btn @click="submitForm" color="primary" depressed>บันทึก</v-btn
            ><v-btn
              @click="gotoPreviuosPage"
              color="primary"
              depressed
              class="buttonleft"
              >ย้อนกลับ</v-btn
            >
          </v-form></v-card-text
        ></validation-observer
      >
    </v-card>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
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
  name: "Skill",
  components: { ValidationObserver, ValidationProvider, Navbar },
  data() {
    return {
      skill: {},
      skills: [],
      accountid: {},
      messagecreate: "",
      title: "ทักษะ",
      headersskill: [
        { text: "ทักษะด้าน", align: "center", sortable: false },
        { text: "รายละเอียด", align: "center", sortable: false },
      ],
    };
  },
  computed: { ...mapState(["APIData"]) },
  created() {
    this.setFormData();
    this.getAPIData();
    setInterval(this.getCreateMessage, 5000);
  },
  methods: {
    submitForm() {
      this.createSkill();
    },
    setFormData() {
      this.skill = {};
      this.getCreateMessage();
    },
    getCreateMessage() {
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "บันทึกไม่สำเร็จเกิดข้อผิดพลาด ลองใหม่อีกครั้ง";
    },
    async getAPIData() {
      await getAPI
        .get("/api/skills/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.skills = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
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
    async createSkill() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/skills/",
          {
            accountid: this.accountid,
            name: this.skill.name,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.getAPIData();
          this.setFormData();
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
