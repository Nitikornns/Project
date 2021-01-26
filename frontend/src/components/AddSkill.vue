<template>
  <v-app>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">ทักษะภาษาโปรแกรมมิ่ง</h2>
      <v-form>
        <validation-provider
          name="รหัสนิสิต"
          :rules="{
            required: true,
            max: 8,
            digits: 8,
          }"
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
        ><v-btn @click="maxbar" class="btn btn-success maxbuttoncenter"
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

extend("digits", {
  ...digits,
  message: "{_field_} เป็นตัวเลข {length} หลัก",
});

extend("required", {
  ...required,
  message: "{_field_} ไม่สามารถเว้นว่างได้",
});

extend("max", {
  ...max,
  message: "{_field_} ไม่เกิน {length} หลัก",
});

extend("regex", {
  ...regex,
  message: "{_field_} {_value_} รูปแบบไม่ถูกต้อง ",
});

extend("email", {
  ...email,
  message: "อีเมลต้องอยู่ในรูปแบบที่ถูกต้อง",
});
export default {
  name: "AddSkill",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      skill: {},
      skills: [],
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  created() {
    this.getSkill();
  },
  methods: {
    submitForm() {
      this.createSkill();
    },
    getSkill() {
      let skills = axios.get("api/skills/").then((r) => r.data);
      this.skills = skills;
      this.skill = { score: 0 };
    },
    createSkill() {
      try {
        axios.post("api/skills/", this.skill).then(window.location.reload());
      } catch (error) {
        this.$dialog.alert("!เพิ่มไม่สำเร็จ รายการนี้มีอยู่ก่อนแล้ว");
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Language" });
    },
    maxbar() {
      this.getSkill();
      this.skill = { score: 100 };
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
</style>
