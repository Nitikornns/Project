import Vue from "vue";
import VueRouter from "vue-router";
import Info from "../views/Info.vue";
import Skill from "../views/Skill.vue";
import Generatepdf from "../views/Generatepdf.vue";
import Language from "../views/Language.vue";
import Education from "../views/Education.vue";
import Picture from "../views/Picture.vue";
import Work from "../views/Work.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";
Vue.use(VueRouter);
export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Info",
      component: Info,
      meta: {
        requiresLogin: true,
      },
    },
    {
      path: "/generatepdf",
      name: "Generatepdf",
      component: Generatepdf,
    },
    {
      path: "/skill",
      name: "Skill",
      component: Skill,
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
    {
      path: "/picture",
      name: "Picture",
      component: Picture,
    },
    {
      path: "/work",
      name: "Work",
      component: Work,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/logout",
      name: "Logout",
      component: Logout,
    },
  ],
});
