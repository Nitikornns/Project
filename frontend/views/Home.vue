<template>
  <v-app class="container">
    <div class="sidenav">
      <div class="login-main-text">
        <h2>
          Application<br />
          Login Page
        </h2>
        <p>Login or register from here to access.</p>
      </div>
    </div>
    <button @click="$router.push('/register')">register</button>
    <button @click="$router.push('/generatepdf')">Generatepdf</button>
    <button @click="$router.push('/ratingskill')">Skill</button>
    <button @click="$router.push('/login')">Login</button>
    <button @click="$router.push('/language')">Language</button>
  </v-app>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style>
body {
  font-family: "Lato", sans-serif;
}

.main-head {
  height: 150px;
  background: #fff;
}

.sidenav {
  height: 100%;
  background-color: #000;
  overflow-x: hidden;
  padding-top: 20px;
  width: 40%;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
}

.main {
  padding: 0px 10px;
}

.login-main-text {
  margin-top: 20%;
  padding: 60px;
  color: #fff;
}

.login-main-text h2 {
  font-weight: 300;
}

.btn-black {
  background-color: #000 !important;
  color: #fff;
}

.a {
  position: relative;
  left: 40%;
  top: 0%;
}

.b {
  background-color: white;
}
</style>
