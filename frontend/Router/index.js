import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import RatingSkills from "../views/RateSkills.vue";
import Generatepdf from "../views/Generatepdf.vue";
import Login from "../views/Login.vue"
import Language from "../views/Language.vue"

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
      path: "/register",
      name: "Register",
      component: Register,
    },
    {
      path: "/ratingskill",
      name: "RatingSkills",
      component: RatingSkills,
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
  ],
});
