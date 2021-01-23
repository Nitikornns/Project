<template>
  <v-app id="app">
    <RatingSkills></RatingSkills>
  </v-app>
</template>

<script>
import RatingSkills from "../src/components/RatingSkills.vue";

export default {
  name: "RateSkills",
  components: { RatingSkills },
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
