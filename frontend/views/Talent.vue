<template>
  <v-app
    ><Navbar></Navbar>
    <v-card weight="1000">
      <v-data-table
        :headers="headerstalent"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr v-for="talent in talents" :key="talent.talentid">
              <td>{{ talent.name }}</td>
              <td>{{ talent.detail }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <v-card-text>
        <h2 style="text-align: center">ความสามารถพิเศษ</h2>
        <h6 class="message">{{ messagecreate }}</h6>
        <br />
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ความสามารถด้าน</v-subheader> </v-col>
            <v-col cols="7">
              <v-text-field v-model="talent.name" outlined dense></v-text-field>
            </v-col>
          </v-row>
          <br />
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>รายอะเอียด</v-subheader> </v-col>
            <v-col cols="7"
              ><v-text-field
                v-model="talent.detail"
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
  name: "Talent",
  components: { Navbar },
  data() {
    return {
      talent: {},
      talents: [],
      accountid: {},
      messagecreate: "",
      headerstalent: [
        { text: "ความสามารถด้าน", align: "center", sortable: false },
        { text: "รายอะเอียด", align: "center", sortable: false },
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
      this.createTalent();
    },
    setFormData() {
      this.talent = {};
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "เกิดความผิดพลาดบันทึกไม่สำเร็จ";
    },
    async getAPIData() {
      await getAPI
        .get("/api/talents/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.talents = this.$store.state.APIData;
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
    async createTalent() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/talents/",
          {
            accountid: this.accountid,
            name: this.talent.name,
            detail: this.talent.detail,
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
