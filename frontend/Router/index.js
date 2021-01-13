import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import RatingSkills from "../views/Skills.vue";

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
      meta: {
        requiresLogin: true,
      },
    },
    {
      path: "/login",
      name: "Login",
    },
    {
      path: "/register",
      name: "Register",
      component: Register,
    },
    {
      path: "/ratingskills",
      name: "RatingSkills",
      component: RatingSkills,
    },
  ],
});
