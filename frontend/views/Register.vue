<template>
  <v-app id="app">
    <Navbar></Navbar>
    <v-card class="mx-auto" width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
      </v-card-title>
      <v-window v-model="step">
        <v-window-item :value="1">
          <v-card-text>
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
            ></v-text-field>
          </v-card-text>
        </v-window-item>

        <v-window-item :value="2">
          <div class="pa-4 text-center">
            <v-img
              class="mb-4"
              contain
              height="128"
              src="https://cdn.vuetifyjs.com/images/logos/v.svg"
            ></v-img>
            <h3 class="title font-weight-light mb-2">
              Welcome to Vuetify
            </h3>
            <span class="caption grey--text">Thanks for signing up!</span>
          </div>
        </v-window-item>
      </v-window>

      <v-divider></v-divider>
      <v-card-actions>
        <v-btn
          :disabled="step === 2"
          color="primary"
          depressed
          @click="createUser"
        >
          ยืนยัน </v-btn
        ><v-spacer></v-spacer
        ><v-btn
          :disabled="step === 1"
          color="primary"
          depressed
          @click="gotoPreviuosPage"
        >
          เข้าสู่ระบบ
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
export default {
  name: "Register",
  data() {
    return {
      account: {},
      show: false,
      step: 1,
      steps: (1, 2),
    };
  },
  components: {
    Navbar,
  },
  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "สมัครสมาชิก";
        default:
          return "สมัครสมาชิกเรียบร้อยแล้ว";
      }
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
        .then(() => {})
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
