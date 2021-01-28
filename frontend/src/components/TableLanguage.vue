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
            @click="deleteItemConfirm(language)"
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
            <h6 class="message">{{ message }}</h6>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="language.name"
                  :items="itemlistlanguages"
                  dense
                  outlined
                >
                </v-select>
              </v-col>
              <v-col cols="12">
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
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="btn btn-success"
            text
            @click="editItemConfirm(language)"
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
          <tr v-for="language in languages" :key="language.languageid">
            <td>{{ language.name }}</td>
            <td>{{ language.sumscore }}</td>
            <v-btn
              fab
              small
              @click="$data.language = language"
              @click.stop="dialogedit = true"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.language = language"
              @click.stop="dialogDelete = true"
            >
              <v-icon small>mdi-delete</v-icon>
            </v-btn>
          </tr>
        </tbody>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">
          <v-btn @click="getLanguage">Refresh</v-btn>
        </v-btn>
      </template>
    </v-data-table>
  </v-app>
</template>
<script>
import axios from "axios";
export default {
  name: "TableLanguage",
  data() {
    return {
      language: {},
      languages: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      message: "",
      headers: [
        { text: "ภาษา", align: "start", sortable: false },
        { text: "ความถนัด (%)", sortable: false },
        { text: "ตัวเลือก", sortable: false },
      ],
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
  created() {
    this.getLanguage();
    this.intervalFetchData();
  },
  methods: {
    async getLanguage() {
      let languages = await axios.get("api/languages/").then((r) => r.data);
      this.languages = languages;
    },
    intervalFetchData() {
      setInterval(this.getLanguage, 1000);
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
      this.message = "ภาษาที่เลือกถูกเพิ่มอยู่ก่อนแล้ว";
    },
    getMessage() {
      this.message = "";
    },
    async deleteItemConfirm(language) {
      try {
        await axios.delete(
          `api/languages/${language.languageid}/`,
          this.language
        );
        this.closeDelete();
        this.getSuccessDeleteMessage();
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(language) {
      try {
        await axios.put(`api/languages/${language.languageid}/`, this.language);
        this.closeEdit();
        this.getMessage();
        this.getSuccessEditMessage();
      } catch (error) {
        this.getFailEditMessage();
      }
    },
    closeDelete() {
      this.dialogDelete = false;
    },
    closeEdit() {
      this.getMessage();
      this.dialogedit = false;
    },
  },
};
</script>
<style scoped>
.message {
  color: red;
}
</style>
