<template>
  <v-app
    ><Navbar></Navbar>
    <v-card weight="1000">
      <v-data-table
        :headers="headerslanguage"
        class="elevation-1"
        hide-default-footer
      >
        <template v-slot:body>
          <tbody>
            <tr v-for="language in languages" :key="language.languageid">
              <td>{{ language.name }}</td>
              <td>{{ language.degree }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
      <v-card-text>
        <h2 style="text-align: center">ทักษะภาษา</h2>
        <h6 class="message">{{ messagecreate }}</h6>
        <v-form>
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ภาษา</v-subheader> </v-col>
            <v-col cols="7">
              <v-selects
                v-model="language.name"
                :options="itemlistlanguages"
              ></v-selects>
            </v-col>
          </v-row>
          <br />
          <v-row align="center" justify="center">
            <v-col cols="3"> <v-subheader>ระดับ</v-subheader> </v-col>
            <v-col cols="7"
              ><v-selects v-model="language.degree" :options="degree">
              </v-selects>
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
import "vue-select/dist/vue-select.css";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
export default {
  name: "Language",
  components: { Navbar },
  data() {
    return {
      language: {},
      languages: [],
      accountid: {},
      messagecreate: "",
      degree: ["พื้นฐานเล็กน้อย", "ปานกลาง", "ดี", "ดีเยี่ยม", "เชี่ยวชาญ"],
      headerslanguage: [
        { text: "ภาษา", align: "center", sortable: false },
        { text: "ระดับความถนัด", align: "center", sortable: false },
      ],
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
    this.getAPIData();
  },
  methods: {
    submitForm() {
      this.createLanguage();
    },
    setFormData() {
      this.language = {};
      this.messagecreate = "";
    },
    getFailCreateMessage() {
      this.messagecreate = "เกิดความผิดพลาดบันทึกไม่สำเร็จ";
    },
    async getAPIData() {
      await getAPI
        .get("/api/languages/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.languages = this.$store.state.APIData;
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
    async createLanguage() {
      await this.getAccountid();
      await axiosBase
        .post(
          "/api/languages/",
          {
            accountid: this.accountid,
            name: this.language.name,
            degree: this.language.degree,
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
