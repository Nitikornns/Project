<template>
  <v-app>
    <Navbar></Navbar>
    <validation-observer class="container d-flex card" ref="observer"
      ><v-form
        ><h2 style="text-align: center">เลือกรูปภาพ</h2>
        <div id="message">
          {{ message }}
        </div>
        <v-file-input
          v-model="picture"
          prepend-icon="mdi-camera"
          placeholder="เลือกรูปภาพ"
          :show-size="1000"
        ></v-file-input>
        <v-btn class="buttonleft" @click="submitForm">บันทึก</v-btn>
        <v-btn @click="deleteItemConfirm">ลบ</v-btn>
        <v-btn class="buttonright" @click="gotoNextPage">ถัดไป</v-btn></v-form
      >
    </validation-observer>
  </v-app>
</template>

<script>
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import { extend, ValidationObserver, setInteractionMode } from "vee-validate";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
import Navbar from "../src/components/Navbar";
export default {
  name: "Picture",
  components: { ValidationObserver, Navbar },
  data: () => ({
    picture: [],
    pictures: [],
    accountid: {},
    message: "",
    studentname: [],
    pictureid: {},
  }),
  computed: {
    ...mapState(["APIData"]),
  },
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
      this.message = "อัพโหลดรูปภาพผิดพลาด";
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
          })
          .catch(() => {
            this.failedMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    async deleteItemConfirm() {
      await this.getPictureid();
      try {
        await axiosBase
          .delete(`api/pictures/${this.pictureid[0].pictureid}/`, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then(() => {
            this.setFormData();
            this.successDeleteMessage();
            this.fetchStatusMessage();
          })
          .catch(() => {});
      } catch (error) {
        console.log(error);
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Generatepdf" });
    },
  },
};
</script>
<style>
.messagesuccess {
  color: green;
}
.messagefail {
  color: red;
}
.buttonleft {
  float: left;
}
.buttonright {
  float: right;
}
.buttoncenter {
  left: 10px;
}
</style>
