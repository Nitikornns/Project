import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
<<<<<<< HEAD
import RatingSkills from "../views/Skills.vue";
=======
import RatingSkills from "../views/RateSkills.vue";
import Generatepdf from "../views/Generatepdf.vue";
>>>>>>> caecf8424281ca9f9be6f3e80b06a37a7c2dc5a8

Vue.use(VueRouter);

export default new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
<<<<<<< HEAD
      meta: {
        requiresLogin: true,
      },
    },
    {
      path: "/login",
      name: "Login",
=======
    },
    {
      path: "/generatepdf",
      name: "Generatepdf",
      component: Generatepdf,
>>>>>>> caecf8424281ca9f9be6f3e80b06a37a7c2dc5a8
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
