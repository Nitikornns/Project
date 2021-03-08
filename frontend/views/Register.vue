<template>
  <v-app id="app">
    <Navbar></Navbar>
    <v-card class="mx-auto" width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ currentTitle }}</span>
        <v-avatar
          color="primary lighten-2"
          class="subheading white--text"
          size="24"
          v-text="step"
        ></v-avatar>
      </v-card-title>
      <v-window v-model="step">
        <v-window-item :value="1">
          <v-card-text
            ><div id="message">{{ message }}</div>
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
              ></v-text-field>
            </v-form>
          </v-card-text>
        </v-window-item>
        <v-window-item :value="2">
          <div class="pa-4 text-center"></div>
        </v-window-item>
      </v-window>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn
          :disabled="step === 2"
          color="primary"
          depressed
          text
          @click="createUser"
        >
          สมัครสมาชิก
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="step === 1"
          color="primary"
          depressed
          @click="gotoLoginPage"
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
    return { account: {}, show: false, step: 1, message: "" };
  },
  components: { Navbar },
  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return "สมัครสมาชิก";
        case 2:
          return "สมัครสมาชิกเรียบร้อนแล้ว";
        default:
          return "Account created";
      }
    },
  },
  methods: {
    getFailMessage() {
      document.getElementById("message").style.color = "red";
      this.message = "อีเมลถูกใช้แล้วหรือกรอกข้อมูลไม่ครบ";
    },
    getStatusMessage() {
      this.message = "";
    },
    createUser() {
      this.$store
        .dispatch("registerUser", {
          email: this.account.email,
          username: this.account.username,
          password: this.account.password,
        })
        .then(() => {
          this.getStatusMessage();
          this.step++;
        })
        .catch((error) => {
          console.log(error);
          this.getFailMessage();
        });
    },
    gotoLoginPage() {
      this.$router.push({ name: "Login" });
    },
  },
};
</script>
<style></style>
