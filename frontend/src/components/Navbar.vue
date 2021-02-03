<template>
  <div class="nav-bar">
    <nav class="navbar navbar-expand-lg navbar-light bg-white nav-1">
      <div class="container mw-0 px-3">
        <v-btn
          v-if="accessToken != null"
          color="accent"
          elevation="5"
          @click="goToLogout"
          >Logout</v-btn
        >
      </div>
    </nav>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "Navbar",
  computed: mapState(["accessToken"]),
  methods: {
    goToLogout() {
      this.$router.push({ name: "Logout" });
    },
  },
};
</script>

<style scoped>
a {
  color: #000;
}
</style>
