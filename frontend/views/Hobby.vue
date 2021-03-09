<template>
  <v-app>
    <Navbar></Navbar>
    <v-card weight="1000">
      <v-data-table
        :headers="headershobby"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr v-for="hobby in hobbies" :key="hobby.hobbyid">
              <td>{{ hobby.name }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <v-card-text>
        <h2 style="text-align: center">งานอดิเรก</h2>
        <h6 class="message">{{ messagecreate }}</h6>
        <br />
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>งานอดิเรก</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field v-model="hobby.name" outlined dense></v-text-field>
            </v-col>
          </v-row>
          <br /><v-btn
            @click="submitForm"
            color="primary"
            class="buttoncenters"
            depressed
            >บันทึก</v-btn
          ><v-btn
            class="buttonleft"
            @click="gotoPreviuosPage"
            color="primary"
            depressed
            >ย้อนกลับ</v-btn
          >
        </v-form>
      </v-card-text>
    </v-card>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import jwt_decode from "jwt-decode";
import { axiosBase, getAPI } from "../axios-api";
import { mapState } from "vuex";
export default {
  name: "Hobby",
  components: { Navbar },
  computed: { ...mapState(["APIData"]) },
  created() {
    this.setFormData();
    this.getAPIData();
  },
  data() {
    return {
      hobby: {},
      hobbies: [],
      accountid: {},
      messagecreate: "",
      headershobby: [{ text: "งานอดิเรก", align: "center", sortable: false }],
    };
  },
  methods: {
    submitForm() {
      this.createHobby();
    },
    setFormData() {
      this.hobby = {};
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "เกิดความผิดพลาดบันทึกไม่สำเร็จ";
    },
    async getAPIData() {
      await getAPI
        .get("/api/hobbies/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.hobbies = this.$store.state.APIData;
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
    async createHobby() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/hobbies/",
          { accountid: this.accountid, name: this.hobby.name },
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
