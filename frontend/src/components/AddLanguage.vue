<template>
  <v-app>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">ทักษะภาษา</h2>
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
            v-model="language.studentname"
            label="รหัสนิสิต"
            outlined
            dense
            :counter="8"
          ></v-text-field>
        </validation-provider>
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
  name: "AddLanguage",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      language: {},
      languages: [],
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
  created() {
    this.getLanguage();
  },
  methods: {
    submitForm() {
      this.createLanguage();
    },
    getLanguage() {
      let languages = axios.get("api/languages/").then((r) => r.data);
      this.languages = languages;
      this.language = { score: 0 };
    },
    createLanguage() {
      try {
        axios
          .post("api/languages/", this.language)
          .then(window.location.reload());
      } catch (error) {
        this.$dialog.alert("!เพิ่มไม่สำเร็จ รายการนี้มีอยู่ก่อนแล้ว");
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Education" });
    },
    maxbar() {
      this.getLanguage();
      this.language = { score: 100 };
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
