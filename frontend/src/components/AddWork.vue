<template>
  <v-app>
    <h6 class="message">{{ messagecreate }}</h6>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">การทำงาน</h2>
      <v-form>
        <v-col cols="12">
          <validation-provider
            name="รหัสนิสิต"
            :rules="{ required: true, max: 8, digits: 8 }"
          >
            <v-text-field
              v-model="work.studentname"
              label="รหัสนิสิต"
              outlined
              dense
              :counter="8"
            ></v-text-field>
          </validation-provider>
          <validation-provider name="ชื่อที่ทำงาน" :rules="{ required: true }">
            <v-text-field
              v-model="work.name"
              label="ชื่อที่ทำงาน"
              outlined
              dense
            ></v-text-field>
          </validation-provider>
          <v-textarea
            v-model="work.detail"
            label="รายละเอียด"
            outlined
            dense
            height="150"
          ></v-textarea>
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
  name: "AddWork",
  components: { ValidationProvider, ValidationObserver },
  data() {
    return { work: {}, message: "" };
  },
  created() {
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createWork();
    },
    getMessage() {
      this.message = "";
    },
    getFailMessage() {
      this.message = "กรอกข้อมูลให้ครบ";
    },
    setFormData() {
      this.work = {};
    },
    async createWork() {
      try {
        await axios.post("api/works/", this.work);
        this.setFormData();
        this.getMessage();
      } catch (error) {
        this.getFailMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Picture" });
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
