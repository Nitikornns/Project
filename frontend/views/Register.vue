<template>
  <v-app id="app">
    <Navbar></Navbar>
    <v-card class="mx-auto" width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ Title }}</span>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="account.email"
            label="อีเมล (ใช้ในการเข้าสู่ระบบ)"
            prepend-inner-icon="mdi-email"
          ></v-text-field>
          <v-text-field
            v-model="account.password"
            label="รหัสผ่าน"
            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
            :type="show ? 'text' : 'password'"
            prepend-inner-icon="mdi-lock"
            @click:append="show = !show"
          ></v-text-field>
          <v-text-field
            v-model="account.username"
            label="ชื่อผู้ใช้"
            prepend-inner-icon="mdi-account"
          ></v-text-field> </v-form
        ><v-btn color="primary" depressed @click="createUser">
          สมัครสมาชิก
        </v-btn>
      </v-card-text>
    </v-card>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
export default {
  name: "Register",
  data() {
    return { account: {}, show: false, step: 1 };
  },
  components: { Navbar },
  computed: {
    Title() {
      return "สมัครสมาชิก";
    },
  },
  methods: {
    createUser() {
      this.$store
        .dispatch("registerUser", {
          email: this.account.email,
          username: this.account.username,
          password: this.account.password,
        })
        .then(() => {
          this.gotoPreviuosPage();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    gotoPreviuosPage() {
      this.$router.push({ name: "Dashboard" });
    },
  },
};
</script>
<style></style>
