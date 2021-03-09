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
              <td>{{ skill.detail }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <hr />
      <h2 style="text-align: center">ทักษะ</h2>
      <v-card-text>
        <h6 class="message">{{ messagecreate }}</h6>
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ทักษะด้าน</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field v-model="skill.name" outlined dense></v-text-field>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>รายละเอียด</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field v-model="skill.detail" outlined dense></v-text-field
            ></v-col>
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
      >
    </v-card>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
export default {
  name: "Skill",
  components: { Navbar },
  data() {
    return {
      skill: {},
      skills: [],
      accountid: {},
      messagecreate: "",
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
            detail: this.skill.detail,
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
