<template>
  <v-app
    ><Navbar></Navbar>
    <v-container class="container d-flex card">
      <h2 style="text-align: center">การศึกษา</h2>
      <h6 class="message">{{ messagecreate }}</h6>
      <v-form>
        <v-col cols="12">
          <v-selects v-model="education.degree" :options="educationdegree">
          </v-selects>
        </v-col>
        <v-col cols="12"
          ><v-text-field
            v-model="education.name"
            label="ชื่อ"
            outlined
            dense
          ></v-text-field
        ></v-col>
        <v-col cols="12"
          ><date-picker
            v-model="education.datestart"
            valueType="format"
            name="วันเริ่ม"
            placeholder="วันเริ่ม"
          ></date-picker>
          <date-picker
            v-model="education.dateend"
            valueType="format"
            name="วันจบ"
            placeholder="วันจบ"
            class="dateend"
          ></date-picker
        ></v-col>
        <br />
        <v-btn @click="submitForm" color="primary" depressed class="buttonleft"
          >บันทึก</v-btn
        ><v-btn
          @click="gotoPreviuosPage"
          color="primary"
          depressed
          class="buttonleft2"
          >ย้อนกลับ</v-btn
        >
      </v-form></v-container
    >
  </v-app>
</template>
<script>
import "vue-select/dist/vue-select.css";
import jwt_decode from "jwt-decode";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
import Navbar from "../src/components/Navbar";
export default {
  name: "Education",
  components: { DatePicker, Navbar },
  data() {
    return {
      education: {},
      messagecreate: "",
      accountid: {},
      educationdegree: [
        "มัธยมศึกษา",
        "ประกาศนียบัตรวิชาชีพ (ปวช.)",
        "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)",
        "ปริญญาตรี",
        "ปริญญาโท",
        "ปริญญาเอก",
      ],
    };
  },
  computed: { ...mapState(["APIData"]) },
  created() {
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createEducation();
    },
    setFormData() {
      this.education = {};
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "กรอกข้อมูลไม่ครบ";
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
    async createEducation() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/educations/",
          {
            accountid: this.accountid,
            educationid: this.education.educationid,
            datestart: this.education.datestart,
            dateend: this.education.dateend,
            name: this.education.name,
            degree: this.education.degree,
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
