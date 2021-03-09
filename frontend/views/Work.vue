<template>
  <v-app
    ><Navbar></Navbar>
    <v-card weight="1000">
      <v-data-table
        :headers="headerswork"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr v-for="work in works" :key="work.workid">
              <td>{{ work.name }}</td>
              <td>{{ work.detail }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <v-card-text>
        <h2 style="text-align: center">ผลงาน</h2>
        <h6 class="message">{{ messagecreate }}</h6>
        <br />
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ผลงาน</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field v-model="work.name" outlined dense></v-text-field>
            </v-col>
          </v-row>
          <br />
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>รายอะเอียด</v-subheader> </v-col>
            <v-col cols="7"
              ><v-text-field
                v-model="work.detail"
                outlined
                dense
              ></v-text-field>
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
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
export default {
  name: "Work",
  components: { Navbar },
  data() {
    return {
      work: {},
      works: [],
      accountid: {},
      messagecreate: "",
      headerswork: [
        { text: "ผลงาน", align: "center", sortable: false },
        { text: "รายอะเอียด", align: "center", sortable: false },
      ],
    };
  },
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
  created() {
    this.setFormData();
    this.getAPIData();
  },
  methods: {
    submitForm() {
      this.createWork();
    },
    setFormData() {
      this.work = {};
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "เกิดความผิดพลาดบันทึกไม่สำเร็จ";
    },
    async getAPIData() {
      await getAPI
        .get("/api/works/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.works = this.$store.state.APIData;
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
    async createWork() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/works/",
          {
            accountid: this.accountid,
            name: this.work.name,
            detail: this.work.detail,
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
