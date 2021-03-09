<template>
  <v-app>
    <Navbar></Navbar>
    <v-card class="container">
      <v-data-table
        :headers="headersexperience"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr
              v-for="experience in experiences"
              :key="experience.experienceid"
            >
              <td>{{ experience.name }}</td>
              <td>{{ experience.datestart }}</td>
              <td>{{ experience.dateend }}</td>
              <td>{{ experience.detail }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <hr />
      <h2 style="text-align: center">ประสบการณ์การทำงาน</h2>
      <v-card-text>
        <h6 class="message">{{ messagecreate }}</h6>
        <v-form
          ><v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>งาน</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field
                v-model="experience.name"
                outlined
                dense
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3">
              <v-subheader>ปีที่เริ่มเข้าทำงาน</v-subheader>
            </v-col>
            <v-col cols="7">
              <v-selects v-model="experience.datestart" :options="years">
              </v-selects>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ปีที่จบจากงาน</v-subheader></v-col>
            <v-col cols="7">
              <v-selects v-model="experience.dateend" :options="years">
              </v-selects>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>รายละเอียด</v-subheader> </v-col>
            <v-col cols="7">
              <v-textarea
                v-model="experience.detail"
                outlined
                dense
                height="150"
              ></v-textarea>
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
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template>
<script>
import "vue-select/dist/vue-select.css";
import Navbar from "../src/components/Navbar";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
export default {
  name: "Experience",
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
      experience: {},
      experiences: [],
      accountid: {},
      messagecreate: "",
      headersexperience: [
        { text: "งาน", align: "center", sortable: false },
        { text: "ปีที่เริ่มเข้าทำงาน", align: "center", sortable: false },
        { text: "ปีที่จบจากงาน", align: "center", sortable: false },
        { text: "รายละเอียด", align: "center", sortable: false },
      ],
    };
  },
  created() {
    this.setFormData();
    this.getAPIData();
    setInterval(this.getCreateMessage, 5000);
  },
  methods: {
    submitForm() {
      this.createExperience();
    },
    setFormData() {
      this.experience = {};
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
        .get("/api/experiences/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.experiences = this.$store.state.APIData;
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
    async createExperience() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/experiences/",
          {
            accountid: this.accountid,
            experienceid: this.experience.experienceid,
            name: this.experience.name,
            datestart: this.experience.datestart,
            dateend: this.experience.dateend,
            detail: this.experience.detail,
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
