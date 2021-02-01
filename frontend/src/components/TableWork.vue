<template>
  <v-app
    ><v-dialog v-model="dialogDelete" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="deleteItemConfirm(work)"
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
            <h6 class="message">{{ messageedit }}</h6>
            <v-col cols="12">
              <v-text-field
                v-model="work.name"
                label="ชื่อที่ทำงาน"
                outlined
                dense
              ></v-text-field>
              <v-textarea
                v-model="work.detail"
                label="รายละเอียด"
                outlined
                dense
                height="150"
              ></v-textarea>
            </v-col>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="editItemConfirm(work)">
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
          <tr v-for="work in works" :key="work.workid">
            <td>{{ work.name }}</td>
            <td>{{ work.detail }}</td>
            <v-btn
              fab
              small
              @click.stop="dialogedit = true"
              @click="$data.work = work"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.work = work"
              @click.stop="dialogDelete = true"
            >
              <v-icon small>mdi-delete</v-icon>
            </v-btn>
          </tr>
        </tbody>
      </template>
    </v-data-table>
  </v-app>
</template>
<script>
import axios from "axios";
export default {
  name: "TableWork",
  components: {},
  data() {
    return {
      work: {},
      works: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      messagecreate: "",
      messageedit: "",
      headers: [
        { text: "ชื่อ", align: "start", sortable: false },
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
    this.getWork();
  },
  methods: {
    async createEducation() {
      try {
        await axios.post("api/works/", this.work);
        this.setFormData();
        this.getMessageCreate();
        this.getWork();
      } catch (error) {
        this.getFailMessage();
      }
    },
    gotoNextPage() {
      this.$router.push({ name: "Work" });
    },
    async getWork() {
      let works = await axios.get("api/works/").then((r) => r.data);
      this.works = works;
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
      this.messageedit = "กรอกข้อมูลให้ครบ";
    },
    getMessageEdit() {
      this.messageedit = "";
    },
    async deleteItemConfirm(work) {
      try {
        await axios.delete(`api/works/${work.workid}/`, this.work);
        this.closeDelete();
        this.getSuccessDeleteMessage();
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(work) {
      try {
        await axios.put(`api/works/${work.workid}/`, this.work);
        this.closeEdit();
        this.getMessageEdit();
        this.getSuccessEditMessage();
      } catch (error) {
        this.getFailEditMessage();
      }
    },
    closeDelete() {
      this.dialogDelete = false;
      this.getWork();
      this.setFormData();
    },
    closeEdit() {
      this.getMessageEdit();
      this.dialogedit = false;
      this.getWork();
      this.setFormData();
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
