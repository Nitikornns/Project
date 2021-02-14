<template>
  <v-app>
    <v-card class="mx-auto" width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
      </v-card-title>
      <h1 class="h3 mb-3 font-weight-normal text-center">เข้าสู่ระบบ</h1>
      <v-card-text>
        <p v-if="incorrectAuth">
          อีเมลหรือรหัสผ่านไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง
        </p>
        <form v-on:submit.prevent="userLogin">
          <div class="form-group">
            <v-text-field
              v-model="email"
              label="อีเมล"
              prepend-inner-icon="mdi-email"
            ></v-text-field>
          </div>
          <div class="form-group">
            <v-text-field
              v-model="password"
              label="รหัสผ่าน"
              :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show ? 'text' : 'password'"
              prepend-inner-icon="mdi-lock"
              @click:append="show = !show"
            ></v-text-field>
          </div>
        </form>
        <v-btn type="submit" color="primary" depressed @click="userLogin">
          เข้าสู่ระบบ
        </v-btn>
        <v-btn
          class="buttonleft"
          @click="gotoRegisterPage"
          color="primary"
          depressed
        >
          สมัครสมาชิก
        </v-btn>
      </v-card-text>
    </v-card>
  </v-app>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      email: "",
      password: "",
      incorrectAuth: false,
      show: false,
      message: "เข้าสู่ระบบ",
    };
  },
  methods: {
    userLogin() {
      this.$store
        .dispatch("userLogin", { email: this.email, password: this.password })
        .then(() => {
          this.$router.push({ name: "Dashboard" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
    gotoRegisterPage() {
      this.$router.push({ name: "Register" });
    },
  },
};
</script>
<style></style>
