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
    <v-dialog
      v-model="dialogedit"
      persistent
      hide-overlay
      scrollable
      max-width="400px"
    >
      <v-card height="400px">
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="languages.studentname"
                  label="รหัสนิสิต"
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-selects
                  v-model="language.name"
                  :options="itemlistlanguages"
                  disabled
                >
                </v-selects>
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
          <v-btn class="btn btn-danger" text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-btn class="btn btn-success" text @click="edit(language)">
            ยืนยัน
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-data-table :headers="headers" sort-by="calories" class="elevation-1">
      <template v-slot:body>
        <tbody>
          <tr v-for="language in languages" :key="language.languageid">
            <td>{{ language.name }}</td>
            <td>{{ language.sumscore }}</td>
            <td>
              <v-icon
                small
                class="mr-2"
                @click.stop="dialogedit = true"
                @click="$data.language = language"
                >mdi-pencil</v-icon
              >
              <v-icon
                small
                @click="$data.language = language"
                @click.stop="dialogDelete = true"
                >mdi-delete</v-icon
              >
            </td>
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
      headers: [
        {
          text: "ภาษา",
          align: "start",
          value: "name",
        },
        { text: "ความถนัด (%)", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
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
  async created() {
    await this.getLanguage();
  },
  methods: {
    async getLanguage() {
      let languages = await axios.get("api/languages/").then((r) => r.data);
      this.languages = languages;
    },
    deleteItemConfirm(language) {
      try {
        axios.delete(`api/languages/${language.languageid}/`, this.language);
        this.getLanguage();
        this.closeDelete();
        this.$dialog.alert("ลบสำเร็จ!");
      } catch (error) {
        this.$dialog.alert("!ลบไม่สำเร็จ");
      }
    },
    edit(language) {
      try {
        axios.put(`api/languages/${language.languageid}/`, this.language);
        this.closeEdit();
        this.getLanguage();
        this.$dialog.alert("แก้ไขสำเร็จ!");
      } catch (error) {
        this.closeEdit();
        this.$dialog.alert("!แก้ไขไม่สำเร็จ รายการซ้ำกับที่มีอยู่");
      }
    },
    closeDelete() {
      this.getLanguage();
      this.dialogDelete = false;
    },
    closeEdit() {
      this.getLanguage();
      this.dialogedit = false;
    },
  },
};
</script>
