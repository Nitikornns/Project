<template>
  <v-app
    ><Navbar></Navbar
    ><v-dialog v-model="dialogDelete" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="btn btn-success"
            text
            @click="deleteItemConfirm(language)"
            >ยืนยัน</v-btn
          >
          <v-btn class="btn btn-danger" text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogedit" persistent max-width="400px">
      <v-card height="320px">
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageedit }}</h6>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="language.name"
                  :items="itemlistlanguages"
                  dense
                  outlined
                >
                </v-select>
              </v-col>
              <v-col cols="12">
                <v-progress-linear
                  v-model="language.score"
                  background-color="#607D8B"
                  color="#E91E63"
                  height="30"
                  class="rounded-pill"
                >
                  <strong>{{ Math.trunc(language.score) }}%</strong>
                </v-progress-linear>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="btn btn-success"
            text
            @click="editItemConfirm(language)"
          >
            ยืนยัน
          </v-btn>
          <v-btn class="btn btn-danger" text @click="closeEdit"> ยกเลิก </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-data-table :headers="headers" class="elevation-1">
      <template v-slot:body>
        <tbody>
          <tr v-for="language in APIData" :key="language.languageid">
            <td>{{ language.name }}</td>
            <td>{{ language.sumscore }}</td>
            <v-btn
              fab
              small
              @click="$data.language = language"
              @click.stop="dialogedit = true"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.language = language"
              @click.stop="dialogDelete = true"
            >
              <v-icon small>mdi-delete</v-icon>
            </v-btn>
          </tr>
        </tbody>
      </template>
    </v-data-table>
    <h6 class="message">{{ messagecreate }}</h6>
    <div class="container d-flex card">
      <h2 style="text-align: center">ทักษะภาษา</h2>
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
          <strong>{{ Math.trunc(language.score) }}%</strong> </v-progress-linear
        ><br /><v-btn @click="submitForm" class="btn btn-success buttonleft"
          >บันทึก</v-btn
        ><v-btn @click="maxBar" class="btn btn-success maxbuttoncenter"
          >100%เต็ม</v-btn
        >
        <v-btn @click="gotoNextPage" class="btn btn-success buttonright"
          >ถัดไป</v-btn
        >
      </v-form>
    </div>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import "vue-select/dist/vue-select.css";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import { extend, setInteractionMode } from "vee-validate";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Language",
  components: { Navbar },
  data() {
    return {
      language: {},
      languages: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messagecreate: "",
      messageedit: "",
      headers: [
        { text: "ภาษา", align: "start", sortable: false },
        { text: "ความถนัด (%)", sortable: false },
        { text: "ตัวเลือก", sortable: false },
      ],
      accountid: {},
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
  computed: {
    ...mapState(["APIData"]),
    formTitle() {
      return this.editedIndex === -1 ? "แก้ไข" : "";
    },
  },
  created() {
    this.getLanguage();
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createLanguage();
    },
    setFormData() {
      this.language = { score: 0 };
      this.getMessageEdit();
      this.getMessageCreate();
    },
    getMessageCreate() {
      this.messagecreate = "";
    },
    getMessageEdit() {
      this.messageedit = "";
    },
    getFailEditMessage() {
      this.messageedit = "ภาษาที่เลือกถูกเพิ่มอยู่ก่อนแล้ว";
    },
    getAlreadyExistMessage() {
      let message = "ข้อมูลไม่ครบหรือเป็นรายการที่มีอยู่แล้ว";
      let options = {
        okText: "ปิด",
        cancelText: "Cancel",
        animation: "bounce",
        type: "basic",
      };
      this.$dialog.alert(message, options);
    },
    getFailDeleteMessage() {
      let message = "ลบไม่สำเร็จ";
      let options = {
        okText: "ปิด",
        cancelText: "Cancel",
        animation: "bounce",
        type: "basic",
      };
      this.$dialog.alert(message, options);
    },
    async getLanguage() {
      await getAPI
        .get("/api/languages/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getAccountid() {
      await getAPI
        .get("/account/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.accountid = response.data;
          return this.accountid;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async createLanguage() {
      await this.getAccountid();
      try {
        await axiosBase
          .post(
            "/api/languages/",
            {
              accountid: this.accountid[0].id,
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
            this.getLanguage();
            this.setFormData();
          })
          .catch(() => {
            this.getLanguage();
            this.getAlreadyExistMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    async deleteItemConfirm(language) {
      await this.getAccountid();
      try {
        await axiosBase
          .delete(`api/languages/${language.languageid}/`, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then(() => {
            this.closeDelete();
            this.setFormData();
          })
          .catch((err) => {
            console.log(err);
          });
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(language) {
      await this.getAccountid();
      let data = {
        accountid: this.accountid[0].id,
        languageid: this.language.languageid,
        name: this.language.name,
        score: this.language.score,
        sumscore: this.language.sumscore,
      };
      try {
        await axiosBase
          .put(`api/languages/${language.languageid}/`, data, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then(() => {
            this.closeEdit();
            this.setFormData();
          })
          .catch((err) => {
            console.log(err);
            this.getLanguage();
            this.getFailEditMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    closeDelete() {
      this.dialogDelete = false;
      this.getLanguage();
      this.setFormData();
    },
    closeEdit() {
      this.dialogedit = false;
      this.getLanguage();
      this.setFormData();
    },
    maxBar() {
      this.language = { score: 100 };
    },
    gotoNextPage() {
      this.$router.push({ name: "Education" });
    },
  },
};
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.buttonleft {
  float: left;
}
.buttonright {
  float: right;
}
.maxbuttoncenter {
  left: 10px;
}
.message {
  color: red;
}
</style>
