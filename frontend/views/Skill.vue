<template
  ><div id="app"><TableSkill></TableSkill><AddSkill></AddSkill></div>
</template>
<script>
import TableSkill from "../src/components/TableSkill.vue";
import AddSkill from "../src/components/AddSkill.vue";
export default {
  name: "Skill",
  components: { TableSkill, AddSkill },
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
