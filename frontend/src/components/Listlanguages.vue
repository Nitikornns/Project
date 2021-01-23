<template>
  <v-app>
    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">ทักษะภาษา</h2>

      <v-simple-table
        fixed-header
        dark
        height="300px"
        class="text-center elevation-1"
      >
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">
                ชื่อภาษา
              </th>
              <th class="text-center">
                ความถนัด(%)
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="language in languages" :key="language.languageid">
              <td>{{ language.name }}</td>
              <td>{{ language.sumscore }}%</td>
              <td>
                <v-icon
                  small
                  class="mr-2"
                  @click="$data.language = language"
                  @click.stop="dialogedit = true"
                >
                  mdi-pencil
                </v-icon>
                <v-icon
                  small
                  @click="$data.language = language"
                  @click.stop="dialogDelete = true"
                >
                  mdi-delete
                </v-icon>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>

      <br />
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
        </v-selects>
        <!-- <v-btn @click="maxbar" class="btn btn-success buttonright">เต็ม</v-btn-->

        <br /><v-progress-linear
          v-model="language.score"
          background-color="#607D8B"
          color="#E91E63"
          height="30"
          class="rounded-pill"
        >
          <strong>{{ Math.trunc(language.score) }}%</strong>
        </v-progress-linear>

        <br /><v-btn
          @click="submitForm"
          :disabled="invalid"
          class="btn btn-success buttonleft"
          >บันทึก</v-btn
        >
        <v-btn @click="gotogeneratepdf" class="btn btn-success buttonright"
          >ถัดไป</v-btn
        >

        <v-dialog v-model="dialogedit" max-width="1000px">
          <v-card height="1000px">
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-col cols="12" sm="6" md="12">
                  <validation-provider
                    name="รหัสนิสิต"
                    :rules="{
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
                </v-col>
                <v-col cols="12" sm="6" md="12">
                  <v-selects
                    v-model="language.name"
                    :options="itemlistlanguages"
                  >
                  </v-selects>
                </v-col>
                <v-col cols="12" sm="6" md="12">
                  <v-progress-linear
                    v-model="language.score"
                    background-color="#607D8B"
                    color="#E91E63"
                    height="30"
                    class="rounded-pill"
                  >
                    <strong>{{ Math.trunc(language.score) }}%</strong>
                  </v-progress-linear>
                </v-col>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <!--<v-btn @click="maxbar" class="btn btn-success buttonright"
                >เต็ม</v-btn
              >-->
              <v-btn
                class="btn btn-success buttonleft"
                text
                @click="save(language)"
              >
                ยินยัน
              </v-btn>

              <v-btn class="btn btn-danger buttonright" text @click="closeEdit">
                ยกเลิก
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline justify-center"
              >ต้องการจะลบใช่หรือไม่?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer
              ><v-btn
                class="btn btn-success buttonleft"
                text
                @click="deleteItemConfirm(language)"
                >ยืนยัน</v-btn
              >
              <v-btn
                class="btn btn-danger buttonright"
                text
                @click="closeDelete"
                >ยกเลิก</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
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
  name: "Listlanguages",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      language: {},
      languages: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      //itemlistlanguages: itemlistlanguages,
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
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "แก้ไข" : "";
    },
  },
  async created() {
    await this.getLanguage();
  },
  methods: {
    submitForm() {
      this.createLanguage();
    },
    async getLanguage() {
      let languages = await axios.get("api/languages/").then((r) => r.data);
      this.languages = languages;
      this.language = { score: 0 };
    },
    async createLanguage() {
      await axios.post("api/languages/", this.language);

      await this.getLanguage();
      this.language = { score: 0 };
    },
    async editlanguage(language) {
      await axios.put(`api/languages/${language.languageid}/`, this.language);

      await this.getLanguage();
      this.closeEdit();
      this.language = { score: 0 };
    },
    async deleteLanguage(language) {
      await axios.delete(
        `api/languages/${language.languageid}/`,
        this.language
      );

      await this.getLanguage();
    },
    gotogeneratepdf() {
      this.$router.push({ name: "Generatepdf" });
    },
    async closeEdit() {
      await this.getLanguage();
      this.dialogedit = false;
    },
    async save(language) {
      if (this.editedIndex > -1) {
        //Object.assign(this.language[this.editedIndex], this.editedItem);
      } else {
        await axios.put(`api/languages/${language.languageid}/`, this.language);

        await this.getLanguage();
        this.language = { score: 0 };
      }
      this.closeEdit();
    },
    async closeDelete() {
      await this.getLanguage();
      this.dialogDelete = false;
    },
    async deleteItemConfirm(language) {
      await axios.delete(
        `api/languages/${language.languageid}/`,
        this.language
      );

      this.getLanguage();
      this.language = {};
      this.closeDelete();
    },
    async maxbar() {
      await this.getLanguage();
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
</style>
