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
            @click="deleteItemConfirm(education)"
            >ยืนยัน</v-btn
          >
          <v-btn class="btn btn-danger" text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogedit" persistent max-width="800px">
      <v-card height="490px">
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageedit }}</h6>
            <v-col cols="12">
              <v-selects v-model="education.degree" :options="educationdegree">
              </v-selects>
            </v-col>
            <v-col cols="12"
              ><v-text-field
                v-model="education.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field
            ></v-col>
            <v-col cols="12"
              ><date-picker
                v-model="education.datestart"
                valueType="format"
                name="วันเริ่ม"
                placeholder="วันเริ่ม"
              ></date-picker>
              <date-picker
                v-model="education.dateend"
                valueType="format"
                name="วันจบ"
                placeholder="วันจบ"
                class="dateend"
              ></date-picker
            ></v-col>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="btn btn-success"
            text
            @click="editItemConfirm(education)"
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
          <tr v-for="education in APIData" :key="education.educationid">
            <td>{{ education.degree }}</td>
            <td>{{ education.name }}</td>
            <td>{{ education.datestart }}</td>
            <td>{{ education.dateend }}</td>
            <v-btn
              fab
              small
              @click.stop="dialogedit = true"
              @click="$data.education = education"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.education = education"
              @click.stop="dialogDelete = true"
            >
              <v-icon small>mdi-delete</v-icon>
            </v-btn>
          </tr>
        </tbody>
      </template>
    </v-data-table>

    <h6 class="message">{{ messagecreate }}</h6>
    <validation-observer class="container d-flex card" ref="observer">
      <h2 style="text-align: center">การศึกษา</h2>
      <v-form>
        <v-col cols="12">
          <v-selects v-model="education.degree" :options="educationdegree">
          </v-selects>
        </v-col>
        <v-col cols="12"
          ><v-text-field
            v-model="education.name"
            label="ชื่อ"
            outlined
            dense
          ></v-text-field
        ></v-col>
        <v-col cols="12"
          ><date-picker
            v-model="education.datestart"
            valueType="format"
            name="วันเริ่ม"
            placeholder="วันเริ่ม"
          ></date-picker>
          <date-picker
            v-model="education.dateend"
            valueType="format"
            name="วันจบ"
            placeholder="วันจบ"
            class="dateend"
          ></date-picker
        ></v-col>
        <br /><v-btn @click="submitForm" class="btn btn-success buttonleft"
          >บันทึก</v-btn
        >
        <v-btn @click="gotoNextPage" class="btn btn-success buttonright"
          >ถัดไป</v-btn
        >
      </v-form>
    </validation-observer>
  </v-app>
</template>

<script>
import "vue-select/dist/vue-select.css";
import jwt_decode from "jwt-decode";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
import Navbar from "../src/components/Navbar";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import { extend, ValidationObserver, setInteractionMode } from "vee-validate";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Education",
  components: { DatePicker, ValidationObserver, Navbar },
  data() {
    return {
      education: {},
      educations: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messagecreate: "",
      messageedit: "",
      accountid: {},
      headers: [
        { text: "ระดับ", align: "start", sortable: false },
        { text: "ชื่อ", sortable: false },
        { text: "วันเริ่ม", sortable: false },
        { text: "วันจบ", sortable: false },
        { text: "ตัวเลือก", sortable: false },
      ],
      educationdegree: [
        "มัธยมศึกษา",
        "ประกาศนียบัตรวิชาชีพ (ปวช.)",
        "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)",
        "ปริญญาตรี",
        "ปริญญาโท",
        "ปริญญาเอก",
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
    this.getEducation();
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createEducation();
    },
    setFormData() {
      this.education = {};
      this.getMessageEdit();
      this.getMessageCreate();
    },
    getMessageCreate() {
      this.messagecreate = "";
    },
    getMessageEdit() {
      this.messageedit = "";
    },
    getFailMessage() {
      this.messagecreate = "กรอกข้อมูลไม่ครบ";
    },
    getFailEditMessage() {
      this.messageedit = "กรอกข้อมูลไม่ครบ";
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
    async getEducation() {
      await getAPI
        .get("/api/educations/", {
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
    async createEducation() {
      await this.getAccountid();
      try {
        await axiosBase
          .post(
            "/api/educations/",
            {
              accountid: this.accountid,
              educationid: this.education.educationid,
              datestart: this.education.datestart,
              dateend: this.education.dateend,
              name: this.education.name,
              degree: this.education.degree,
            },
            {
              headers: {
                Authorization: `Bearer ${this.$store.state.accessToken}`,
              },
            }
          )
          .then(() => {
            this.setFormData();
            this.getEducation();
          })
          .catch(() => {
            this.getEducation();
            this.getAlreadyExistMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    async deleteItemConfirm(education) {
      await this.getAccountid();
      try {
        await axiosBase
          .delete(`api/educations/${education.educationid}/`, {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          })
          .then(() => {
            this.closeDelete();
            this.setFormData();
          })
          .catch(() => {
            this.closeDelete();
            this.getFailDeleteMessage();
          });
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(education) {
      await this.getAccountid();
      try {
        await axiosBase
          .put(
            `api/educations/${education.educationid}/`,
            {
              accountid: this.accountid,
              educationid: this.education.educationid,
              datestart: this.education.datestart,
              dateend: this.education.dateend,
              name: this.education.name,
              degree: this.education.degree,
            },
            {
              headers: {
                Authorization: `Bearer ${this.$store.state.accessToken}`,
              },
            }
          )
          .then(() => {
            this.closeEdit();
            this.setFormData();
          })
          .catch((err) => {
            console.log(err);
            this.getEducation();
            this.getFailEditMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    closeDelete() {
      this.dialogDelete = false;
      this.getEducation();
      this.setFormData();
    },
    closeEdit() {
      this.dialogedit = false;
      this.getEducation();
      this.setFormData();
    },
    gotoNextPage() {
      this.$router.push({ name: "Work" });
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
.dateend {
  left: 10px;
}
.message {
  color: red;
}
.buttonleft {
  float: left;
}
.buttonright {
  float: right;
}
</style>
