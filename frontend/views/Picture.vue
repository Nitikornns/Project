<template>
  <v-app>
    <Navbar></Navbar>
    <div class="container d-flex card">
      <v-form
        ><h2 style="text-align: center">เลือกรูปภาพ</h2>
        <div id="message">{{ message }}</div>
        <v-file-input
          v-model="picture"
          prepend-icon="mdi-camera"
          placeholder="เลือกรูปภาพ"
          :show-size="1000"
        ></v-file-input>
        <v-btn color="primary" depressed @click="submitForm">บันทึก</v-btn>
        <v-btn
          @click="gotoPreviuosPage"
          color="primary"
          depressed
          class="buttonleft"
          >ย้อนกลับ</v-btn
        >
      </v-form>
    </div>
  </v-app>
</template>
<script>
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
import Navbar from "../src/components/Navbar";
export default {
  name: "Picture",
  components: { Navbar },
  data: () => ({ picture: [], accountid: {}, message: "", pictureid: {} }),
  computed: { ...mapState(["APIData"]) },
  methods: {
    submitForm() {
      this.submitFile();
    },
    setStatusMessage() {
      this.message = "";
    },
    fetchStatusMessage() {
      setInterval(this.setStatusMessage, 5000);
    },
    successMessage() {
      document.getElementById("message").style.color = "green";
      this.message = "อัพโหลดรูปภาพสำเร็จ";
    },
    successDeleteMessage() {
      document.getElementById("message").style.color = "green";
      this.message = "ลบรูปภาพสำเร็จ";
    },
    failedMessage() {
      document.getElementById("message").style.color = "red";
      this.message = "อัพโหลดรูปภาพผิดพลาด กดบันทึกอีกครั้ง";
    },
    setFormData() {
      this.picture = [];
      this.message = "";
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
    async getPictureid() {
      await getAPI
        .get("/api/pictures/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.pictureid = response.data;
          return this.pictureid;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async submitFile() {
      await this.getAccountid();
      try {
        let formData = new FormData();
        formData.append("accountid", this.accountid);
        formData.append("picturefile", this.picture);
        await axiosBase
          .post("/api/pictures/", formData, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then(() => {
            this.successMessage();
            this.gotoPreviuosPage();
          })
          .catch(() => {
            this.failedMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Generatepdf" });
    },
    gotoPreviuosPage() {
      this.$router.push({ name: "Dashboard" });
    },
  },
};
</script>
