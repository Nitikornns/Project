<template>
  <v-app>
    <Navbar></Navbar>
    <div class="container d-flex card">
      <h2 style="text-align: center">ทักษะภาษาโปรแกรมมิ่ง</h2>
      <h6 class="message">{{ messagecreate }}</h6>
      <v-form>
        <v-selects v-model="skill.name" :options="itemlistskill"> </v-selects
        ><br />
        <v-progress-linear
          v-model="skill.score"
          background-color="#607D8B"
          color="#E91E63"
          height="30"
          class="rounded-pill"
        >
          <strong>{{ Math.trunc(skill.score) }}</strong> </v-progress-linear
        ><br />
        <v-btn @click="submitForm" color="primary" depressed class="buttonleft"
          >บันทึก</v-btn
        ><v-btn
          @click="gotoPreviuosPage"
          color="primary"
          depressed
          class="buttonleft2"
          >ย้อนกลับ</v-btn
        >
        ><v-btn @click="maxBar" color="primary" depressed class="buttonright"
          >100เต็ม</v-btn
        >
      </v-form>
    </div>
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
      this.skill = { score: 0 };
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
    async createSkill() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/skills/",
          {
            accountid: this.accountid,
            name: this.skill.name,
            score: this.skill.score,
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
    maxBar() {
      this.skill = { score: 100 };
    },
    gotoPreviuosPage() {
      this.$router.push({ name: "Dashboard" });
    },
  },
};
</script>
