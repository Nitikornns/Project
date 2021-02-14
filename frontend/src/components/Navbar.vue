<template>
  <div class="nav-bar">
    <v-toolbar
      dark
      src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    >
      <v-btn plain :to="{ name: 'Dashboard' }"
        ><v-icon>mdi-home</v-icon>
        หน้าหลัก
      </v-btn>
      <ul v-if="accessToken != null">
        <v-btn plain icon :to="{ name: 'Generatepdf' }"
          ><v-icon>mdi-file-pdf</v-icon>บันทึกข้อมูลเป็นไฟล์pdf
        </v-btn>
      </ul>
      <v-spacer></v-spacer>
      <ul v-if="accessToken != null">
        <v-btn plain icon :to="{ name: 'Logout' }"
          ><v-icon>mdi-export</v-icon>ออกจากระบบ
        </v-btn>
      </ul>
    </v-toolbar>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default { name: "Navbar", computed: mapState(["accessToken"]) };
</script>
<style>
@import url(https://fonts.googleapis.com/css?family=Quicksand);
.nav-bar {
  background-color: #2f3033;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  overflow: hidden;
}
.nav-bar ul {
  list-style: none;
  margin: 0 14%;
  padding: 0;
  text-align: center;
  color: white;
}
.nav-bar ul li {
  display: inline-block;
  margin: 0 5px;
  padding: 25px;
  float: right;
  left: 100%;
}
.nav-bar:after {
  content: "";
  display: block;
  clear: both;
}
.nav-bar ul li a {
  text-decoration: none;
  font-family: "Quicksand", sans-serif;
  font-size: 22px;
  font-weight: bold;
  color: white;
  padding: 10px;
  border-radius: 7px;
}
.nav-bar ul li a:hover {
  background-color: #a72a64;
}
.router-link-active {
  background-color: #a72a64;
}
</style>
