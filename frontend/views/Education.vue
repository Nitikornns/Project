<template>
  <v-app
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
              <v-text-field
                v-model="education.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field>
              <v-textarea
                v-model="education.detail"
                label="รายละเอียด"
                outlined
                dense
                height="150"
              ></v-textarea>
              <date-picker
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
              ></date-picker>
            </v-col>
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
          <tr v-for="education in educations" :key="education.educationid">
            <td>{{ education.name }}</td>
            <td>{{ education.datestart }}</td>
            <td>{{ education.dateend }}</td>
            <td>{{ education.detail }}</td>
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
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">การศึกษา</h2>
      <v-form>
        <v-col cols="12">
          <validation-provider
            name="รหัสผู้ใช้"
            :rules="{ required: true, max: 8, digits: 8 }"
          >
            <v-text-field
              v-model="education.studentname"
              label="รหัสผู้ใช้"
              outlined
              dense
              :counter="8"
            ></v-text-field>
          </validation-provider>
          <validation-provider name="ชื่อ" :rules="{ required: true }">
            <v-text-field
              v-model="education.name"
              label="ชื่อ"
              outlined
              dense
            ></v-text-field>
          </validation-provider>
          <v-textarea
            v-model="education.detail"
            label="รายละเอียด"
            outlined
            dense
            height="150"
          ></v-textarea>
          <date-picker
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
          ></date-picker>
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
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
setInteractionMode("eager");
extend("digits", { ...digits, message: "{_field_} เป็นตัวเลข {length} หลัก" });
extend("required", { ...required, message: "{_field_} ไม่สามารถเว้นว่างได้" });
extend("max", { ...max, message: "{_field_} ไม่เกิน {length} หลัก" });
extend("regex", { ...regex, message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง " });
extend("email", { ...email, message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง" });
export default {
  name: "Education",
  components: { DatePicker, ValidationProvider, ValidationObserver },
  data() {
    return {
      education: {},
      educations: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messagecreate: "",
      messageedit: "",
      headers: [
        { text: "ชื่อ", align: "start", sortable: false },
        { text: "วันเริ่ม", sortable: false },
        { text: "วันจบ", sortable: false },
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
    this.getEducation();
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createEducation();
    },
    getMessageCreate() {
      this.messagecreate = "";
    },
    getFailMessage() {
      this.messagecreate = "กรอกข้อมูลให้ครบ";
    },
    setFormData() {
      this.education = {};
      this.getMessageEdit();
      this.getMessageCreate();
    },
    async createEducation() {
      try {
        await axios.post("api/educations/", this.education);
        this.setFormData();
        this.getEducation();
      } catch (error) {
        this.getFailMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Work" });
    },
    async getEducation() {
      let educations = await axios.get("api/educations/").then((r) => r.data);
      this.educations = educations;
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
    async deleteItemConfirm(education) {
      try {
        await axios.delete(
          `api/educations/${education.educationid}/`,
          this.education
        );
        this.closeDelete();
        this.getSuccessDeleteMessage();
        this.setFormData();
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(education) {
      try {
        await axios.put(
          `api/educations/${education.educationid}/`,
          this.education
        );
        this.closeEdit();
        this.setFormData();
        this.getSuccessEditMessage();
      } catch (error) {
        this.getFailEditMessage();
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
