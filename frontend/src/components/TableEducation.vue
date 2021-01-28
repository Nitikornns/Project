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
            <h6 class="message">{{ message }}</h6>
            <v-col cols="12">
              <v-text-field
                v-model="education.schoolname"
                label="ชื่อโรงเรียน"
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
            <td>{{ education.schoolname }}</td>
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
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">
          <v-btn @click="getEducation">Refresh</v-btn>
        </v-btn>
      </template>
    </v-data-table>
  </v-app>
</template>
<script>
import axios from "axios";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
export default {
  name: "TableEducation",
  components: { DatePicker },
  data() {
    return {
      education: {},
      educations: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      message: "",
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
    this.intervalFetchData();
  },
  methods: {
    async getEducation() {
      let educations = await axios.get("api/educations/").then((r) => r.data);
      this.educations = educations;
    },
    intervalFetchData() {
      setInterval(this.getEducation, 1000);
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
      this.message = "กรอกข้อมูลให้ครบ";
    },
    getMessage() {
      this.message = "";
    },
    async deleteItemConfirm(education) {
      try {
        await axios.delete(
          `api/educations/${education.educationid}/`,
          this.education
        );
        this.closeDelete();
        this.getSuccessDeleteMessage();
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
.dateend {
  left: 10px;
}
.message {
  color: red;
}
</style>
