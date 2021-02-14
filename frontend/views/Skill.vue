<template>
  <v-app>
    <Navbar></Navbar>
    <v-card weight="1000">
      <v-card-text>
        <h2 style="text-align: center">ทักษะภาษาโปรแกรมมิ่ง</h2>
        <h6 class="message">{{ messagecreate }}</h6>
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ภาษา</v-subheader> </v-col>
            <v-col cols="7">
              <v-selects v-model="skill.name" :options="itemlistskill">
              </v-selects>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ระดับ</v-subheader> </v-col>
            <v-col cols="7">
              <v-selects v-model="skill.degree" :options="degree"> </v-selects
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
import "vue-select/dist/vue-select.css";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
export default {
  name: "Skill",
  components: { Navbar },
  data() {
    return {
      skill: {},
      accountid: {},
      messagecreate: "",
      messageedit: "",
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
      degree: ["พื้นฐานเล็กน้อย", "ปานกลาง", "ดี", "ดีเยี่ยม", "เชี่ยวชาญ"],
    };
  },
  computed: { ...mapState(["APIData"]) },
  created() {
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createSkill();
    },
    setFormData() {
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "เกิดความผิดพลาดบันทึกไม่สำเร็จ";
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
            degree: this.skill.degree,
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
