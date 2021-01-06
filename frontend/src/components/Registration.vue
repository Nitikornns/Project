<template>
  <v-app id="app">
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
            :key="student.userid"
            @dblclick="$data.student = student"
          >
            <td>{{ student.userid }}</td>
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

    <validation-observer
      class="container d-flex card"
      ref="observer"
      v-slot="{ invalid }"
    >
      <h2 style="text-align: center">กรอกข้อมูล</h2>
      <v-form @submit.prevent="submitForm">
        <v-container>
          <validation-provider
            v-slot="{ errors }"
            name="รหัสนิสิต"
            :rules="{
              required: true,
              max: 8,
              digits: 8,
            }"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>รหัสนิสิต</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.userid"
                  outlined
                  dense
                  :error-messages="errors"
                  required
                  :counter="8"
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="ชั้นปี"
            rules="required"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ชั้นปี</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-select
                  v-model="student.year"
                  :items="yearsitem"
                  dense
                  outlined
                  :error-messages="errors"
                  required
                ></v-select>
              </v-col>
            </v-row>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="ชื่อจริง"
            rules="required|max:100"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ชื่อ</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.name"
                  :error-messages="errors"
                  required
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="นามสกุล"
            rules="required|max:100"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>นามสกุล</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.surname"
                  outlined
                  dense
                  :error-messages="errors"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="เลขบัตรประชาชน"
            :rules="{
              required: true,
              max: 13,
              digits: 13,
            }"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>เลขบัตรประชาชน</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.idcard"
                  outlined
                  dense
                  required
                  :error-messages="errors"
                  :counter="13"
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="อีเมล"
            rules="required|email"
          >
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>อีเมล</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.email"
                  outlined
                  dense
                  :error-messages="errors"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="เบอร์โทรศัพท์"
            :rules="{
              required: true,
              max: 10,
              digits: 10,
              regex: '0',
            }"
            ><v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>เบอร์โทรศัพท์</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.telphoneNumber"
                  outlined
                  dense
                  required
                  :error-messages="errors"
                  :counter="10"
                ></v-text-field>
              </v-col>
            </v-row>
          </validation-provider>
        </v-container>
        <v-btn type="submit" :disabled="invalid" class="btn btn-success"
          >บันทึก</v-btn
        >
      </v-form>
    </validation-observer>
  </v-app>
</template>

<script>
import axios from "axios";
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
  message: "Email must be valid",
});

export default {
  name: "Registration",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      student: {},
      students: [],
      yearsitem: ["1", "2", "3", "4"],
    };
  },
  async created() {
    await this.getStudents();
  },

  methods: {
    submitForm() {
      this.createStudent();
    },
    async getStudents() {
      let students = await axios.get("api/students/").then((r) => r.data);
      console.log(students);
      this.students = students;
    },

    async createStudent() {
      //await this.getStudents();

      await axios
        .post("api/students/", this.student)
        .then(alert("บันทึกข้อมูลเรียบร้อยแล้ว"));

      await this.getStudents();
      this.student = {};
    },
    async deleteStudent(student) {
      //await this.getStudents();

      await axios.delete(
        `http://localhost:8000/api/students/${student.userid}/`,
        this.student
      );

      await this.getStudents();
      this.student = {};
    },
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>