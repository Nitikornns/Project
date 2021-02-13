<template>
  <v-app
    ><Navbar></Navbar>
    <div class="container d-flex card">
      <h2 style="text-align: center">ทักษะภาษา</h2>
      <h6 class="message">{{ messagecreate }}</h6>
      <v-form>
        <v-selects v-model="language.name" :options="itemlistlanguages">
        </v-selects
        ><br />
        <v-progress-linear
          v-model="language.score"
          background-color="#607D8B"
          color="#E91E63"
          height="30"
          class="rounded-pill"
        >
          <strong>{{ Math.trunc(language.score) }}</strong></v-progress-linear
        ><br /><v-btn
          @click="submitForm"
          color="primary"
          depressed
          class="buttonleft"
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
import jwt_decode from "jwt-decode";
import "vue-select/dist/vue-select.css";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
export default {
  name: "Language",
  components: { Navbar },
  data() {
    return {
      language: {},
      accountid: {},
      messagecreate: "",
      itemlistlanguages: [
        "กัมพูชา",
        "กาตาร์",
        "เกาหลีใต้",
        "เกาหลีเหนือ",
        "คาซัคสถาน",
        "คีร์กีซสถาน",
        "คูเวต",
        "จอร์เจีย",
        "จอร์แดน",
        "จีน",
        "ซาอุดีอาระเบีย",
        "ซีเรีย",
        "ไซปรัส",
        "ญี่ปุ่น",
        "ติมอร์ตะวันออกติมอร์-เลสเต",
        "ตุรกี",
        "เติร์กเมนิสถาน",
        "ไต้หวัน",
        "ทาจิกิสถาน",
        "ไทย",
        "เนปาล",
        "บรูไน",
        "บังกลาเทศ",
        "บาห์เรน",
        "ปากีสถาน",
        "ปาเลสไตน์",
        "ฝรั่งเศษ",
        "พม่าเมียนมา",
        "ฟิลิปปินส์",
        "ภูฏาน",
        "มองโกเลีย",
        "มัลดีฟส์",
        "มาเลเซีย",
        "เยเมน",
        "ลาว",
        "เลบานอน",
        "เวียดนาม",
        "ศรีลังกา",
        "สหรัฐอาหรับเอมิเรตส์",
        "สิงคโปร์",
        "อัฟกานิสถาน",
        "อาเซอร์ไบจาน",
        "อาร์มีเนีย",
        "อินเดีย",
        "อินโดนีเซีย",
        "อิรัก",
        "อิสราเอล",
        "อิหร่าน",
        "อุซเบกิสถาน",
        "โอมาน",
        "อังกฤษ",
      ],
    };
  },
  computed: { ...mapState(["APIData"]) },
  created() {
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createLanguage();
    },
    setFormData() {
      this.language = { score: 0 };
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
    async createLanguage() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/languages/",
          {
            accountid: this.accountid,
            name: this.language.name,
            score: this.language.score,
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
      this.language = { score: 100 };
    },
    gotoPreviuosPage() {
      this.$router.push({ name: "Dashboard" });
    },
  },
};
</script>
