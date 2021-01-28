<template>
  <v-app
    ><v-dialog v-model="dialogDelete" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="deleteItemConfirm(skill)"
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
                  v-model="skill.name"
                  :items="itemlistskill"
                  dense
                  outlined
                >
                </v-select>
              </v-col>
              <v-col cols="12">
                <v-progress-linear
                  v-model="skill.score"
                  background-color="#607D8B"
                  color="#E91E63"
                  height="30"
                  class="rounded-pill"
                >
                  <strong>{{ Math.trunc(skill.score) }}%</strong>
                </v-progress-linear>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="btn btn-success" text @click="editItemConfirm(skill)">
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
          <tr v-for="skill in skills" :key="skill.skillid">
            <td>{{ skill.name }}</td>
            <td>{{ skill.sumscore }}</td>
            <v-btn
              fab
              small
              @click="$data.skill = skill"
              @click.stop="dialogedit = true"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>
            <v-btn
              fab
              small
              @click="$data.skill = skill"
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
  name: "TableLanguage",
  data() {
    return {
      skill: {},
      skills: [],
      dialogedit: false,
      dialogDelete: false,
      editedIndex: -1,
      message: "",
      headers: [
        { text: "ภาษา", align: "start", sortable: false },
        { text: "ความถนัด (%)", sortable: false },
        { text: "ตัวเลือก", sortable: false },
      ],
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "แก้ไข" : "";
    },
  },
  created() {
    this.getSkill();
    this.intervalFetchData();
  },
  methods: {
    async getSkill() {
      let skills = await axios.get("api/skills/").then((r) => r.data);
      this.skills = skills;
    },
    intervalFetchData() {
      setInterval(this.getSkill, 1000);
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
    async deleteItemConfirm(skill) {
      try {
        await axios.delete(`api/skills/${skill.skillid}/`, this.skill);
        this.closeDelete();
        this.getSuccessDeleteMessage();
      } catch (error) {
        this.closeDelete();
        this.getFailDeleteMessage();
      }
    },
    async editItemConfirm(skill) {
      try {
        await axios.put(`api/skills/${skill.skillid}/`, this.skill);
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
