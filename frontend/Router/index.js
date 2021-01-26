import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Info from "../views/Info.vue";
import Skill from "../views/Skill.vue";
import Generatepdf from "../views/Generatepdf.vue";
import Login from "../views/Login.vue"
import Language from "../views/Language.vue"
import Education from "../views/Education.vue"

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/generatepdf",
      name: "Generatepdf",
      component: Generatepdf,
    },
    {
      path: "/info",
      name: "Info",
      component: Info,
    },
    {
      path: "/skill",
      name: "Skill",
      component: Skill,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/language",
      name: "Language",
      component: Language,
    },
    {
      path: "/education",
      name: "Education",
      component: Education,
    },
  ],
});
