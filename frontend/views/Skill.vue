<template>
  <v-app id="app">
    <Navbar></Navbar>
    <v-dialog v-model="dialogDelete" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="deleteItemConfirm(skill)"
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
                  v-model="skill.name"
                  :items="itemlistskill"
                  dense
                  outlined
                >
                </v-select>
              </v-col>
              <v-col cols="12">
                <v-progress-linear
                  v-model="skill.score"
                  background-color="#607D8B"
                  color="#E91E63"
                  height="30"
                  class="rounded-pill"
                >
                  <strong>{{ Math.trunc(skill.score) }}</strong>
                </v-progress-linear>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="editItemConfirm(skill)">
            ยืนยัน
          </v-btn>
          <v-btn class="btn btn-danger" text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-data-table :headers="headers" class="elevation-1">
      <template v-slot:body>
        <tbody>
          <tr v-for="skill in APIData" :key="skill.skillid">
            <td>{{ skill.name }}</td>
            <td>{{ skill.sumscore }}</td>
            <v-btn
              fab
              small
              @click="$data.skill = skill"
              @click.stop="dialogedit = true"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.skill = skill"
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
      <h2 style="text-align: center">ทักษะภาษาโปรแกรมมิ่ง</h2>
      <v-form>
        <v-selects v-model="skill.name" :options="itemlistskill"> </v-selects
        ><br />
        <v-progress-linear
          v-model="skill.score"
          background-color="#607D8B"
          color="#E91E63"
          height="30"
          class="rounded-pill"
        >
          <strong>{{ Math.trunc(skill.score) }}</strong> </v-progress-linear
        ><br /><v-btn @click="submitForm" class="btn btn-success buttonleft"
          >บันทึก</v-btn
        ><v-btn @click="maxBar" class="btn btn-success maxbuttoncenter"
          >100เต็ม</v-btn
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
import jwt_decode from "jwt-decode";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Skill",
  onIdle() {
    this.$store.dispatch("userLogout").then(() => {
      this.$router.push({ name: "login" });
    });
  },
  components: { Navbar },
  data() {
    return {
      skill: {},
      accountid: {},
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messagecreate: "",
      messageedit: "",
      headers: [
        { text: "ภาษา", align: "start", sortable: false },
        { text: "ระดับความถนัด", sortable: false },
        { text: "ตัวเลือก", sortable: false },
      ],
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  computed: {
    ...mapState(["APIData"]),
    formTitle() {
      return this.editedIndex === -1 ? "แก้ไข" : "";
    },
  },
  created() {
    this.getSkill();
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createSkill();
    },
    setFormData() {
      this.skill = { score: 0 };
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
    async getSkill() {
      await getAPI
        .get("/api/skills/", {
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
    async createSkill() {
      await this.getAccountid();
      try {
        await axiosBase
          .post(
            "/api/skills/",
            {
              accountid: this.accountid,
              name: this.skill.name,
              score: this.skill.score,
            },
            {
              headers: {
                Authorization: `Bearer ${this.$store.state.accessToken}`,
              },
            }
          )
          .then(() => {
            this.getSkill();
            this.setFormData();
          })
          .catch(() => {
            this.getSkill();
            this.getAlreadyExistMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    async deleteItemConfirm(skill) {
      await this.getAccountid();
      try {
        await axiosBase
          .delete(`api/skills/${skill.skillid}/`, {
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
    async editItemConfirm(skill) {
      await this.getAccountid();
      try {
        await axiosBase
          .put(
            `api/skills/${skill.skillid}/`,
            {
              accountid: this.accountid,
              skillid: this.skill.skillid,
              name: this.skill.name,
              score: this.skill.score,
              sumscore: this.skill.sumscore,
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
            this.getSkill();
            this.getFailEditMessage();
          });
      } catch (error) {
        console.log(error);
      }
    },
    closeDelete() {
      this.dialogDelete = false;
      this.getSkill();
      this.setFormData();
    },
    closeEdit() {
      this.dialogedit = false;
      this.getSkill();
      this.setFormData();
    },
    maxBar() {
      this.skill = { score: 100 };
    },
    gotoNextPage() {
      this.$router.push({ name: "Language" });
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
