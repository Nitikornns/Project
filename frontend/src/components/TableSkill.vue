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
                  v-model="skill.studentname"
                  label="รหัสนิสิต"
                  outlined
                  dense
                  disabled
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-selects
                  v-model="skill.name"
                  :options="itemlistskill"
                  disabled
                >
                </v-selects>
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
          <v-btn class="btn btn-danger" text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-btn class="btn btn-success" text @click="edit(skill)">
            ยืนยัน
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-data-table :headers="headers" sort-by="calories" class="elevation-1">
      <template v-slot:body>
        <tbody>
          <tr v-for="skill in skills" :key="skill.skillid">
            <td>{{ skill.name }}</td>
            <td>{{ skill.sumscore }}</td>

            <v-btn
              fab
              small
              class="v-data-footer__icons-after"
              @click.stop="dialogedit = true"
              @click="$data.skill = skill"
            >
              <v-icon small>mdi-pencil</v-icon>
            </v-btn>

            <v-btn
              fab
              small
              class="v-data-footer__icons-after"
              @click="$data.skill = skill"
              @click.stop="dialogDelete = true"
            >
              <v-icon small>mdi-delete</v-icon>
            </v-btn>
          </tr>
        </tbody>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">
          <v-btn @click="getSkill">Refresh</v-btn>
        </v-btn>
      </template>
    </v-data-table>
  </v-app>
</template>
<script>
import axios from "axios";
export default {
  name: "TableSkill",
  data() {
    return {
      skill: {},
      skills: [],
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
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "แก้ไข" : "";
    },
  },
  async created() {
    await this.getSkill();
  },
  methods: {
    async getSkill() {
      let skills = await axios.get("api/skills/").then((r) => r.data);
      this.skills = skills;
    },
    deleteItemConfirm(skill) {
      try {
        axios.delete(`api/skills/${skill.skillid}/`, this.skill);
        this.getSkill();
        this.closeDelete();
        this.$dialog.alert("ลบสำเร็จ!");
      } catch (error) {
        this.$dialog.alert("!ลบไม่สำเร็จ");
      }
    },
    edit(skill) {
      try {
        axios.put(`api/skills/${skill.skillid}/`, this.skill);
        this.closeEdit();
        this.getSkill();
        this.$dialog.alert("แก้ไขสำเร็จ!");
      } catch (error) {
        this.closeEdit();
        this.$dialog.alert("!แก้ไขไม่สำเร็จ รายการซ้ำกับที่มีอยู่");
      }
    },
    closeDelete() {
      this.getSkill();
      this.dialogDelete = false;
    },
    closeEdit() {
      this.getSkill();
      this.dialogedit = false;
    },
  },
};
</script>
