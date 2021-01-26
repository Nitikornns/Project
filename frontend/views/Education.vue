<template>
  <v-app id="app">
    <TableEducation></TableEducation><AddEducation></AddEducation>
  </v-app>
</template>

<script>
import AddEducation from "../src/components/AddEducation.vue";
import TableEducation from "../src/components/TableEducation.vue";
export default {
  name: "Education",
  components: { AddEducation, TableEducation },
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
