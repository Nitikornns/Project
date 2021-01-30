<template>
  <div>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <div id="message">
        {{ message }}
      </div>
      <validation-provider
        name="รหัสนิสิต"
        :rules="{ required: true, max: 8, digits: 8 }"
      >
        <v-text-field
          v-model="studentname"
          label="รหัสนิสิต"
          outlined
          dense
          :counter="8"
        ></v-text-field>
      </validation-provider>
      <v-file-input
        v-model="picture"
        prepend-icon="mdi-camera"
        placeholder="เลือกรูปภาพ"
        :show-size="1000"
      ></v-file-input>
      <v-btn @click="submitForm" :disabled="invalid">Submit</v-btn>
      <v-btn @click="gotoNextPage" class="btn btn-success buttonright"
        >ถัดไป</v-btn
      >
    </validation-observer>
  </div>
</template>

<script>
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
import axios from "axios";
export default {
  name: "Picture",
  components: { ValidationProvider, ValidationObserver },
  data: () => ({
    picture: [],
    pictures: [],
    message: "",
    studentname: [],
  }),
  created() {
    this.getPicture();
  },
  methods: {
    submitForm() {
      this.submitFile();
    },
    SuccessMessage() {
      document.getElementById("message").style.color = "green";
      this.message = "อัพโหลดรูปสำเร็จ";
    },
    FailedMessage() {
      document.getElementById("message").style.color = "red";
      this.message = "อัพโหลดรูปผิดพลาด";
    },
    SetFormData() {
      this.picture = [];
      this.studentname = [];
    },
    async submitFile() {
      try {
        let formData = new FormData();
        formData.append("picturefile", this.picture);
        formData.append("studentname", this.studentname);
        await axios.post("api/pictures/", formData);
        this.SuccessMessage();
        this.SetFormData();
      } catch (error) {
        this.FailedMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Generatepdf" });
    },
    async getPicture() {
      let pictures = await axios.get("api/pictures/").then((r) => r.data);
      this.pictures = pictures;
    },
  },
};
</script>
<style>
.messagesuccess {
  color: green;
}
.messagefail {
  color: red;
}
</style>
