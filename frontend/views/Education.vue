<template>
  <v-app
    ><Navbar></Navbar>
    <v-card class="text-center">
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
      <v-card-text>
        <h2 style="text-align: center">การศึกษา</h2>
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
            <v-col cols="3"> <v-subheader>ชื่อ</v-subheader> </v-col>
            <v-col cols="7"
              ><v-text-field
                v-model="education.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>วันเริ่ม</v-subheader> </v-col>
            <v-col cols="7">
              <v-selects v-model="education.datestart" :options="years">
              </v-selects>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>วันจบ</v-subheader></v-col>
            <v-col cols="7">
              <v-selects v-model="education.dateend" :options="years">
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
      let today = new Date();
      let year = today.getFullYear();
      return Array.from(
        { length: year - 1900 },
        (value, index) => 1901 + index
      );
    },
  },
  data() {
    return {
      year: [],
      education: {},
      educations: [],
      accountid: {},
      headerseducation: [
        { text: "ระดับ", align: "center", sortable: false },
        { text: "ชื่อ", align: "center", sortable: false },
        { text: "วันเริ่ม", align: "center", sortable: false },
        { text: "วันจบ", align: "center", sortable: false },
      ],
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
      this.messagecreate = "เกิดความผิดพลาดบันทึกไม่สำเร็จ";
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
