<template>
  <v-app>
    <h6 class="message">{{ message }}</h6>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">การศึกษา</h2>
      <v-form>
        <v-col cols="12">
          <validation-provider
            name="รหัสนิสิต"
            :rules="{ required: true, max: 8, digits: 8 }"
          >
            <v-text-field
              v-model="education.studentname"
              label="รหัสนิสิต"
              outlined
              dense
              :counter="8"
            ></v-text-field>
          </validation-provider>
          <validation-provider name="ชื่อโรงเรียน" :rules="{ required: true }">
            <v-text-field
              v-model="education.schoolname"
              label="ชื่อโรงเรียน"
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
  name: "AddEducation",
  components: { DatePicker, ValidationProvider, ValidationObserver },
  data() {
    return { education: {}, educations: [], message: "" };
  },
  created() {
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createEducation();
    },
    getMessage() {
      this.message = "";
    },
    getFailMessage() {
      this.message = "กรอกข้อมูลให้ครบ";
    },
    setFormData() {
      this.education = {};
    },
    async createEducation() {
      try {
        await axios.post("api/educations/", this.education);
        this.setFormData();
        this.getMessage();
      } catch (error) {
        this.getFailMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Generatepdf" });
    },
  },
};
</script>
<style scoped>
.buttonleft {
  float: left;
}
.buttonright {
  float: right;
}
.message {
  color: red;
}
</style>
