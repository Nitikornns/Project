<template>
  <v-app
    ><Navbar></Navbar>
    <v-card class="container">
      <v-data-table
        :headers="headerseducation"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr v-for="education in educations" :key="education.educationid">
              <td>{{ education.degree }}</td>
              <td>{{ education.name }}</td>
              <td>{{ education.datestart }}</td>
              <td>{{ education.dateend }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <hr />
      <h2 style="text-align: center">{{ title }}</h2>
      <v-card-text>
        <h6 class="message">{{ messagecreate }}</h6>
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ระดับ</v-subheader> </v-col>
            <v-col cols="7"
              ><v-selects v-model="education.degree" :options="educationdegree">
              </v-selects>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>สถานศึกษา</v-subheader></v-col>
            <v-col cols="7"
              ><v-text-field
                v-model="education.name"
                outlined
                dense
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ปีที่เข้าศึกษา</v-subheader> </v-col>
            <v-col cols="7">
              <v-selects v-model="education.datestart" :options="years">
              </v-selects>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ปีที่จบการศึกษา</v-subheader></v-col>
            <v-col cols="7">
              <v-selects
                v-model="education.dateend"
                placeholder="หากยังคงอยู่ในช่วงศึกษาให้เว้นว่าง"
                :options="years"
              >
              </v-selects>
            </v-col>
          </v-row>
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
      ></v-card
    >
  </v-app>
</template>
<script>
import "vue-select/dist/vue-select.css";
import jwt_decode from "jwt-decode";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import Navbar from "../src/components/Navbar";
export default {
  name: "Education",
  components: { Navbar },
  computed: {
    ...mapState(["APIData"]),
    years() {
      let year = new Date().getFullYear();
      return Array.from(
        { length: year - 1900 },
        (value, index) => 1901 + index
      );
    },
  },
  data() {
    return {
      education: {},
      educations: [],
      accountid: {},
      messagecreate: "",
      title: "การศึกษา",
      headerseducation: [
        { text: "ระดับ", align: "center", sortable: false },
        { text: "สถานศึกษา", align: "center", sortable: false },
        { text: "ปีที่เข้าศึกษา", align: "center", sortable: false },
        { text: "ปีที่จบการศึกษา", align: "center", sortable: false },
      ],
      educationdegree: [
        "มัธยมศึกษาตอนต้น",
        "มัธยมศึกษาตอนปลาย",
        "ประกาศนียบัตรวิชาชีพ (ปวช.)",
        "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)",
        "ปริญญาตรี",
        "ปริญญาโท",
        "ปริญญาเอก",
      ],
    };
  },
  created() {
    this.setFormData();
    this.getAPIData();
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
      this.messagecreate = "บันทึกไม่สำเร็จเกิดข้อผิดพลาด ลองใหม่อีกครั้ง";
    },
    async getAPIData() {
      await getAPI
        .get("/api/educations/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.educations = this.$store.state.APIData;
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
          this.setFormData();
          this.getAPIData();
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
