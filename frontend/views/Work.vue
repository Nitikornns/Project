<template>
  <v-app
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
          <tr v-for="work in works" :key="work.workid">
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

    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">การทำงาน</h2>
      <v-form>
        <v-col cols="12">
          <validation-provider
            name="รหัสผู้ใช้"
            :rules="{ required: true, max: 8, digits: 8 }"
          >
            <v-text-field
              v-model="work.studentname"
              label="รหัสผู้ใช้"
              outlined
              dense
              :counter="8"
            ></v-text-field>
          </validation-provider>
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
        <br /><v-btn
          @click="submitForm"
          :disabled="invalid"
          class="btn btn-success buttonleft"
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
import axios from "axios";
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
  components: { ValidationProvider, ValidationObserver },
  data() {
    return {
      work: {},
      works: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messageedit: "",
      headers: [
        { text: "ชื่อ", align: "start", sortable: false },
        { text: "รายละเอียด", sortable: false },
        { text: "ตัวเลือก", sortable: false },
      ],
    };
  },
  computed: {
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
      this.createEducation();
    },
    setFormData() {
      this.work = {};
      this.getMessageEdit();
    },
    async createEducation() {
      try {
        await axios.post("api/works/", this.work);
        this.setFormData();
        this.getWork();
      } catch (error) {
        this.getFailMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Picture" });
    },
    async getWork() {
      let works = await axios.get("api/works/").then((r) => r.data);
      this.works = works;
    },
    getSuccessDeleteMessage() {
      this.$dialog.alert("ลบสำเร็จ");
    },
    getFailDeleteMessage() {
      this.$dialog.alert("ลบไม่สำเร็จ");
    },
    getSuccessEditMessage() {
      this.$dialog.alert("แก้ไขสำเร็จ");
    },
    getFailEditMessage() {
      this.messageedit = "กรอกข้อมูลให้ครบ";
    },
    getMessageEdit() {
      this.messageedit = "";
    },
    async deleteItemConfirm(work) {
      try {
        await axios.delete(`api/works/${work.workid}/`, this.work);
        this.closeDelete();
        this.getSuccessDeleteMessage();
        this.setFormData();
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(work) {
      try {
        await axios.put(`api/works/${work.workid}/`, this.work);
        this.closeEdit();
        this.setFormData();
        this.getSuccessEditMessage();
      } catch (error) {
        this.getFailEditMessage();
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
