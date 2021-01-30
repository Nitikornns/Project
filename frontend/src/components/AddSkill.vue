<template>
  <v-app>
    <h6 class="message">{{ message }}</h6>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">ทักษะภาษาโปรแกรมมิ่ง</h2>
      <v-form>
        <validation-provider
          name="รหัสนิสิต"
          :rules="{ required: true, max: 8, digits: 8 }"
        >
          <v-text-field
            v-model="skill.studentname"
            label="รหัสนิสิต"
            outlined
            dense
            :counter="8"
          ></v-text-field>
        </validation-provider>
        <v-selects v-model="skill.name" :options="itemlistskill"> </v-selects
        ><br />
        <v-progress-linear
          v-model="skill.score"
          background-color="#607D8B"
          color="#E91E63"
          height="30"
          class="rounded-pill"
        >
          <strong>{{ Math.trunc(skill.score) }}%</strong> </v-progress-linear
        ><br /><v-btn
          @click="submitForm"
          :disabled="invalid"
          class="btn btn-success buttonleft"
          >บันทึก</v-btn
        ><v-btn @click="maxBar" class="btn btn-success maxbuttoncenter"
          >100%เต็ม</v-btn
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
import "vue-select/dist/vue-select.css";
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
  name: "AddLanguage",
  components: { ValidationProvider, ValidationObserver },
  data() {
    return {
      skill: {},
      message: "",
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  created() {
    this.setFormData();
  },
  methods: {
    submitForm() {
      this.createSkill();
    },
    intervalFetchMessage() {
      setInterval(this.getMessage, 5000);
    },
    getMessage() {
      this.message = "";
    },
    getFailMessage() {
      this.message = "เพิ่มไม่สำเร็จ รายการนี้มีอยู่ก่อนแล้ว";
    },
    setFormData() {
      this.skill = { score: 0 };
    },
    maxBar() {
      this.skill = { score: 100 };
    },
    async createSkill() {
      try {
        await axios.post("api/skills/", this.skill);
        this.setFormData();
        this.getMessage();
      } catch (error) {
        this.getFailMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Language" });
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
.maxbuttoncenter {
  left: 10px;
}
.message {
  color: red;
}
</style>
