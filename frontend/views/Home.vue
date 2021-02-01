<template>
  <v-app>
    <Info></Info>
  </v-app>
</template>

<script>
import Info from "../views/Info.vue";
export default {
  name: "Home",
  components: { Info },
};
</script>

<style>
body {
  font-family: "Lato", sans-serif;
}
</style>
