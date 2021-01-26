<template>
  <v-app id="app">
    <AddInfo></AddInfo>
  </v-app>
</template>

<script>
import AddInfo from "../src/components/AddInfo.vue";
export default {
  name: "Info",
  components: { AddInfo },
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
