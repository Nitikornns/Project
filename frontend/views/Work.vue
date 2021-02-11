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
          <v-btn class="btn btn-success" text @click="deleteItemConfirm(work)"
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
              <v-text-field
                v-model="work.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field>
              <v-textarea
                v-model="work.detail"
                label="รายละเอียด"
                outlined
                dense
                height="150"
              ></v-textarea>
            </v-col>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="editItemConfirm(work)">
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
          <tr v-for="work in APIData" :key="work.workid">
            <td>{{ work.name }}</td>
            <td>{{ work.detail }}</td>
            <v-btn
              fab
              small
              @click.stop="dialogedit = true"
              @click="$data.work = work"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.work = work"
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
      <h2 style="text-align: center">การทำงาน</h2>
      <v-form>
        <v-col cols="12">
          <validation-provider name="ชื่อ" :rules="{ required: true }">
            <v-text-field
              v-model="work.name"
              label="ชื่อ"
              outlined
              dense
            ></v-text-field>
          </validation-provider>
          <validation-provider name="ชื่อ" :rules="{ required: true }">
            <v-textarea
              v-model="work.detail"
              label="รายละเอียด"
              outlined
              dense
              height="150"
            ></v-textarea>
          </validation-provider>
        </v-col>
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
import Navbar from "../src/components/Navbar";
import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Work",
  components: { ValidationProvider, ValidationObserver, Navbar },
  data() {
    return {
      work: {},
      works: [],
      accountid: {},
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messagecreate: "",
      messageedit: "",
      headers: [
        { text: "ชื่อ", align: "start", sortable: false },
        { text: "รายละเอียด", sortable: false },
        { text: "ตัวเลือก", sortable: false },
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
    this.getWork();
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createWork();
    },
    setFormData() {
      this.work = {};
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
      this.messageedit = "กรอกข้อมูลไม่ครบ";
    },
    getFailMessage() {
      this.messagecreate = "กรอกข้อมูลไม่ครบ";
    },
    async getWork() {
      await getAPI
        .get("/api/works/", {
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
    async createWork() {
      await this.getAccountid();
      try {
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
            this.getWork();
          })
          .catch(() => {
            this.getWork();
            this.getFailMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    async deleteItemConfirm(work) {
      await this.getAccountid();
      try {
        await axiosBase
          .delete(`api/works/${work.workid}/`, {
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
    async editItemConfirm(work) {
      await this.getAccountid();
      try {
        await axiosBase
          .put(
            `api/works/${work.workid}/`,
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
            this.closeEdit();
            this.setFormData();
          })
          .catch((err) => {
            console.log(err);
            this.getWork();
            this.getFailEditMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    closeDelete() {
      this.dialogDelete = false;
      this.getWork();
      this.setFormData();
    },
    closeEdit() {
      this.dialogedit = false;
      this.getWork();
      this.setFormData();
    },
    gotoNextPage() {
      this.$router.push({ name: "Picture" });
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
