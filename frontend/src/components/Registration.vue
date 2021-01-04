<template>
  <div id="app">
    <table class="table">
      <thead>
        <th>รหัสนิสิต</th>
        <th>ชื่อ</th>
        <th>นามสกุล</th>
        <th>เลขบัตรประชาชน</th>
        <th>วันจบการศึกษา</th>
        <th>อีเมล</th>
        <th>เบอร์โทรศัพท์</th>
      </thead>
      <tbody>
        <tr
          v-for="student in students"
          :key="student.userid"
          @dblclick="$data.student = student"
        >
          <td>{{ student.userid }}</td>
          <td>{{ student.name }}</td>
          <td>{{ student.surname }}</td>
          <td>{{ student.idcard }}</td>
          <td>{{ student.commencementday }}</td>
          <td>{{ student.email }}</td>
          <td>{{ student.telphoneNumber }}</td>
          <td>
            <button
              class="btn btn-outline-danger btn-sm mx-1"
              @click="deleteStudent(student)"
            >
              X
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="container d-flex justify-content-center card">
      <h2>Register</h2>

      <form @submit.prevent="submitForm">
        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Student Code</label>
            <input
              type="text"
              class="form-control"
              placeholder="รหัสนิสิต"
              v-model="student.userid"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Year</label>
            <select class="form-control" v-model="student.year" required>
              <option disabled value="">ชั้นปี</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Passwords</label>
            <input
              type="text"
              class="form-control"
              placeholder="รหัสผ่าน"
              v-model="student.password"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Name</label>
            <input
              type="text"
              class="form-control"
              placeholder="ชื่อจริง"
              v-model="student.name"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Surname</label>
            <input
              type="text"
              class="form-control"
              placeholder="นามสกุล"
              v-model="student.surname"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Id card</label>
            <input
              type="text"
              class="form-control"
              placeholder="เลขบัตรประชาชน"
              v-model="student.idcard"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Email</label>
            <input
              type="text"
              class="form-control"
              placeholder="อีเมล"
              v-model="student.email"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <div class="form-row col-md-12">
            <label>Telephone Number</label>
            <input
              type="text"
              class="form-control"
              placeholder="เบอร์โทรศัพท์"
              v-model="student.telphoneNumber"
              required
            />
          </div>
        </div>

        <button class="btn btn-success">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Registration",
  data() {
    return {
      student: {},
      students: [],
    };
  },
  async created() {
    await this.getStudents();
  },
  methods: {
    submitForm() {
      if (this.student.userid !== undefined) {
        this.createStudent();
      } else {
        //alert("This Student Code already exists");
        //this.editStudent();
      }
    },
    async getStudents() {
      var response = await fetch("http://localhost:8000/api/students/");
      this.students = await response.json();
    },
    async createStudent() {
      await this.getStudents();

      await fetch("http://localhost:8000/api/students/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });
      alert("Registration Completed success");
      await this.getStudents();
      this.student = {};
    },
    async editStudent() {
      await this.getStudents();

      await fetch(
        `http://localhost:8000/api/students/${this.student.userid}/`,
        {
          method: "save",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.student),
        }
      );

      await this.getStudents();
      this.student = {};
    },
    async deleteStudent(student) {
      await this.getStudents();

      await fetch(`http://localhost:8000/api/students/${student.userid}/`, {
        method: "delete",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.student),
      });

      await this.getStudents();
      this.student = {};
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>