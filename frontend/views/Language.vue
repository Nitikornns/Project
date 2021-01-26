<template>
  <v-app id="app">
    <TableLanguage></TableLanguage><AddLanguage></AddLanguage>
  </v-app>
</template>
<script>
import TableLanguage from "../src/components/TableLanguage";
import AddLanguage from "../src/components/AddLanguage";
export default {
  name: "Language",
  components: {
    AddLanguage,
    TableLanguage,
  },
};
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
