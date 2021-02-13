import Vue from "vue";
import VueRouter from "vue-router";
import Info from "./views/Info.vue";
import Skill from "./views/Skill.vue";
import Generatepdf from "./views/Generatepdf.vue";
import Language from "./views/Language.vue";
import Education from "./views/Education.vue";
import Picture from "./views/Picture.vue";
import Work from "./views/Work.vue";
import Login from "./views/Login.vue";
import Logout from "./views/Logout.vue";
import Register from "./views/Register.vue";
import Dashboard from "./views/Dashboard.vue";

Vue.use(VueRouter);
export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/login",
      name: "Login",
      component: Login,
      meta: {
        requiresLogged: true,
      },
    },
    {
      path: "/",
      name: "Dashboard",
      component: Dashboard,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/logout",
      name: "Logout",
      component: Logout,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/register",
      name: "Register",
      component: Register,
      meta: {
        requiresLogged: true,
      },
    },

    {
      path: "/info",
      name: "Info",
      component: Info,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/skill",
      name: "Skill",
      component: Skill,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/language",
      name: "Language",
      component: Language,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/education",
      name: "Education",
      component: Education,
      meta: {
        requiresAuth: true,
      },
    },

    {
      path: "/work",
      name: "Work",
      component: Work,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/picture",
      name: "Picture",
      component: Picture,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/generatepdf",
      name: "Generatepdf",
      component: Generatepdf,
      meta: {
        requiresAuth: true,
      },
    },
  ],
});
