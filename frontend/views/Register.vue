<template>
  <v-app id="app">
    <div>
      <div class="container text-dark">
        <div class="row justify-content-md-center">
          <div class="col-md-5 p-3 login justify-content-md-center">
            <h1 class="h3 mb-3 font-weight-normal text-center">
              สมัครสมาชิก
            </h1>
            <form v-on:submit.prevent="createUser">
              <div class="form-group">
                <v-text-field
                  v-model="account.email"
                  filled
                  label="อีเมล(ใช้ในการเข้าสู่ระบบ)"
                  prepend-inner-icon="mdi-email"
                ></v-text-field>
              </div>
              <div class="form-group">
                <v-text-field
                  v-model="account.username"
                  filled
                  label="ชื่อผู้ใช้"
                  prepend-inner-icon="mdi-account"
                ></v-text-field>
              </div>
              <div class="form-group">
                <v-text-field
                  v-model="account.password"
                  filled
                  label="รหัสผ่าน"
                  :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                  :type="show ? 'text' : 'password'"
                  prepend-inner-icon="mdi-lock"
                  @click:append="show = !show"
                ></v-text-field>
              </div>
              <button type="submit" class="btn btn-lg btn-primary btn-block">
                sign up
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
  name: "Register",
  data() {
    return {
      account: [],
      show: false,
    };
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
          this.$router.push({ name: "Login" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style></style>
