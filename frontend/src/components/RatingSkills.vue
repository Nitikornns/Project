<template >
  <v-app
    ><h2>ทักษะภาษาโปรแกรม</h2>
    <v-simple-table dark dense class="text-center">
      <template v-slot:default>
        <thead>
          <tr>
            <th>ชื่อภาษาโปรแกรม</th>
            <th>ระดับความถนัด</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="skill in skills"
            :key="skill.skillid"
            @dblclick="$data.skill = skill"
          >
            <td>{{ skill.languagename }}</td>
            <td>{{ skill.score }}</td>

            <td>
              <v-btn
                class="btn btn-outline-danger btn-sm mx-1"
                @click="deleteSkill(skill)"
              >
                X
              </v-btn>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>

    <v-container>
      <v-form>
        <v-selects
          v-model="skill.languagename"
          :options="lanname"
          dense
          outlined
          required
        ></v-selects>

        <v-rating
          v-model="skill.score"
          background-color="purple lighten-3"
          color="purple"
          small
        ></v-rating>

        <v-btn @click="createskills">บันทึก</v-btn>
      </v-form>
    </v-container>
  </v-app>
</template>


<script>
import axios from "axios";
import "vue-select/dist/vue-select.css";

export default {
  name: "RatingSkills",
  data() {
    return {
      skill: {},
      skills: [],
      lanname: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  async created() {
    await this.getskill();
  },
  methods: {
    submitForm() {
      this.createskills();
    },
    async getskill() {
      let skills = await axios.get("api/skills/").then((r) => r.data);
      console.log(skills);
      this.skills = skills;
    },
    async createskills() {
      await axios
        .post("api/skills/", this.skill)
        .then(console.log(this.skill))
        .catch(alert("กรุณาเข้าสู่ระบบ"));

      await this.getskill();
      this.skill = {};
    },
    async deleteSkill(skill) {
      await axios.delete(`api/skills/${skill.skillid}/`, this.skill);

      await this.getskill();
      this.skill = {};
    },
  },
};
</script>

<style scoped>
</style>