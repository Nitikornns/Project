<template>
  <v-app>
    <Navbar></Navbar>
    <v-card class="text-center">
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
              <v-btn
                @click.stop="dialogeditwork = true"
                @click="$data.work = work"
                color="success"
              >
                <v-icon small>mdi-pencil</v-icon>แก้ไข
              </v-btn>
              <v-btn
                @click="$data.work = work"
                @click.stop="dialogDeletework = true"
                color="red"
              >
                <v-icon small>mdi-delete</v-icon>ลบ
              </v-btn>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <h2 style="text-align: center">การทำงาน</h2>
      <h6 class="message">{{ messagecreate }}</h6>
      <v-card-text>
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ชื่อสถานที่</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field
                v-model="work.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>รายละเอียด</v-subheader> </v-col>
            <v-col cols="7">
              <v-textarea
                v-model="work.detail"
                label="รายละเอียด"
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
import Navbar from "../src/components/Navbar";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
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
        { text: "ชื่อ", align: "center", sortable: false },
        { text: "รายละเอียด", align: "center", sortable: false },
      ],
    };
  },
  computed: { ...mapState(["APIData"]) },
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
            workid: this.work.workid,
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
