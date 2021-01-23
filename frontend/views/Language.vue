<template>
  <v-app id="app">
    <Listlanguages></Listlanguages>
  </v-app>
</template>

<script>
import Listlanguages from "../src/components/Listlanguages";
export default {
  name: "Language",
  components: { Listlanguages },
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
