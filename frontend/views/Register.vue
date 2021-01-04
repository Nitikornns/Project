<template>
  <div id="app">
    <Registration></Registration>
  </div>
</template>

<script>
import Registration from "../src/components/Registration.vue";
export default {
  components: { Registration },
  name: "Register",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
