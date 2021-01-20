<template>
  <v-app>
    <button @click="generateReport">ดาวโหลดpdf</button>
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="true"
      :preview-modal="true"
      :paginate-elements-by-height="1400"
      filename="MyCV"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a4"
      pdf-orientation="landscape"
      pdf-content-width="800px"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
        <v-simple-table dark dense class="text-center">
          <template v-slot:default>
            <thead>
              <tr>
                <th>รหัสนิสิต</th>
                <th>ชั้นปี</th>
                <th>ชื่อ</th>
                <th>นามสกุล</th>
                <th>เลขบัตรประชาชน</th>
                <th>วันจบการศึกษา</th>
                <th>อีเมล</th>
                <th>เบอร์โทรศัพท์</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="student in students"
                :key="student.studentcode"
                @dblclick="$data.student = student"
              >
                <td>{{ student.studentcode }}</td>
                <td>{{ student.year }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.surname }}</td>
                <td>{{ student.idcard }}</td>
                <td>{{ student.commencementday }}</td>
                <td>{{ student.email }}</td>
                <td>{{ student.telphoneNumber }}</td>
                <td>
                  <v-btn
                    class="btn btn-outline-danger btn-sm mx-1"
                    @click="deleteStudent(student)"
                  >
                    X
                  </v-btn>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
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
      </section>
    </vue-html2pdf>
  </v-app>
</template>


<script>
import axios from "axios";
import VueHtml2pdf from "vue-html2pdf";
export default {
  name: "Pdf",
  components: {
    VueHtml2pdf,
  },
  data() {
    return {
      student: {},
      students: [],
      skill: {},
      skills: [],
    };
  },
  async created() {
    await this.getStudents();
    await this.getskill();
  },
  methods: {
    generateReport() {
      this.$refs.html2Pdf.generatePdf();
    },
    async getStudents() {
      let students = await axios.get("api/students/").then((r) => r.data);
      this.students = students;
    },
    async getskill() {
      let skills = await axios.get("api/skills/").then((r) => r.data);
      this.skills = skills;
    },
  },
};
</script>