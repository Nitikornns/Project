<template>
  <v-app id="app">
    <Registration></Registration>
  </v-app>
</template>

<script>
import Registration from "../src/components/Registration.vue";
export default {
  components: { Registration },
  name: "Register",
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
