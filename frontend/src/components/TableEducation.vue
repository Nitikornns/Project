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
    <v-dialog
      v-model="dialogedit"
      persistent
      hide-overlay
      scrollable
      max-width="800px"
    >
      <v-card height="550px">
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-col cols="12">
              <v-text-field
                v-model="education.studentname"
                label="รหัสนิสิต"
                outlined
                dense
                disabled
              ></v-text-field>

              <v-text-field
                v-model="education.schoolname"
                label="ชื่อโรงเรียน"
                outlined
                dense
                disabled
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
          <v-btn class="btn btn-danger" text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-btn class="btn btn-success" text @click="edit(education)">
            ยืนยัน
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-data-table :headers="headers" sort-by="calories" class="elevation-1">
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
      headers: [
        {
          text: "ชื่อ",
          align: "start",
          value: "name",
        },
        { text: "วันเริ่ม", sortable: false },
        { text: "วันจบ", sortable: false },
        { text: "รายละเอียด", sortable: false },
        { text: "Actions", value: "actions", sortable: false },
      ],
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "แก้ไข" : "";
    },
  },
  async created() {
    await this.getEducation();
  },
  methods: {
    async getEducation() {
      let educations = await axios.get("api/educations/").then((r) => r.data);
      this.educations = educations;
    },
    deleteItemConfirm(education) {
      try {
        axios.delete(
          `api/educations/${education.educationid}/`,
          this.education
        );
        this.getEducation();
        this.closeDelete();
        this.$dialog.alert("ลบสำเร็จ!");
      } catch (error) {
        this.$dialog.alert("!ลบไม่สำเร็จ");
      }
    },
    edit(education) {
      try {
        axios.put(`api/educations/${education.educationid}/`, this.education);
        this.closeEdit();
        this.getEducation();
        this.$dialog.alert("แก้ไขสำเร็จ!");
      } catch (error) {
        this.closeEdit();
        this.$dialog.alert("!แก้ไขไม่สำเร็จ รายการซ้ำกับที่มีอยู่");
      }
    },
    closeDelete() {
      this.getEducation();
      this.dialogDelete = false;
    },
    closeEdit() {
      this.getEducation();
      this.dialogedit = false;
    },
  },
};
</script>
<style scoped>
.dateend {
  left: 10px;
}
</style>
