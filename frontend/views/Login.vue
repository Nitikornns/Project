<template>
  <v-app id="app">
    <div>
      <div class="container text-dark">
        <div class="row justify-content-md-center">
          <div class="col-md-5 p-3 login justify-content-md-center">
            <h1 class="h3 mb-3 font-weight-normal text-center">
              กรุณาเข้าสู่ระบบ
            </h1>

            <p v-if="incorrectAuth">
              อีเมลหรือรหัสผ่านไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง
            </p>
            <form v-on:submit.prevent="login">
              <div class="form-group">
                <v-text-field
                  v-model="email"
                  filled
                  label="อีเมล"
                  prepend-inner-icon="mdi-email"
                ></v-text-field>
              </div>
              <div class="form-group">
                <v-text-field
                  v-model="password"
                  filled
                  label="รหัสผ่าน"
                  :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show ? 'text' : 'password'"
                  prepend-inner-icon="mdi-lock"
                  @click:append="show = !show"
                ></v-text-field>
              </div>
              <button type="submit" class="btn btn-lg btn-primary btn-block">
                Login
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </v-app>
</template>
<script>
export default {
  name: "login",
  data() {
    return { email: "", password: "", incorrectAuth: false, show: false };
  },
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", { email: this.email, password: this.password })
        .then(() => {
          this.$router.push({ name: "Info" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
};
</script>
<style></style>
