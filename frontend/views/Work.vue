<template>
  <v-app
    ><Navbar></Navbar>
    <v-card class="container">
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
      <hr />
      <validation-observer
        class="container d-flex card text-center"
        ref="observer"
      >
        <h2 style="text-align: center">ผลงาน</h2>
        <v-card-text>
          <h6 class="message">{{ messagecreate }}</h6>
          <v-form>
            <validation-provider
              v-slot="{ errors }"
              name="ผลงาน"
              rules="required|max:100"
            >
              <v-row align="center" justify="center">
                <v-col cols="3"> <v-subheader>ผลงาน</v-subheader> </v-col>
                <v-col cols="7">
                  <v-text-field
                    v-model="work.name"
                    outlined
                    :error-messages="errors"
                    required
                    dense
                  ></v-text-field>
                </v-col>
              </v-row>
            </validation-provider>
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
      </validation-observer>
    </v-card>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import jwt_decode from "jwt-decode";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Work",
  components: { ValidationObserver, ValidationProvider, Navbar },
  data() {
    return {
      work: {},
      works: [],
      accountid: {},
      messagecreate: "",
      title: "ผลงาน",
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
    setInterval(this.getCreateMessage, 5000);
  },
  methods: {
    submitForm() {
      this.createWork();
    },
    getSuccessCreateMessage() {
      let message = "เพิ่มข้อมูลสำเร็จ";
      let options = {
        okText: "ปิด",
        cancelText: "Cancel",
        animation: "bounce",
        type: "basic",
      };
      this.$dialog.alert(message, options);
    },
    setFormData() {
      this.work = {};
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
          this.gotoPreviuosPage();
          this.getSuccessCreateMessage();
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
