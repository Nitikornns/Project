import Vue from "vue";
import App from "./App.vue";
import router from "../routes";
import axios from "axios";
import vSelect from "vue-select";
import VuejsDialog from "vuejs-dialog";
import "vuejs-dialog/dist/vuejs-dialog.min.css";
import store from "../store.js";
import vuetify from "@/plugins/vuetify";
import IdleVue from "idle-vue";

axios.defaults.baseURL = process.env.VUE_APP_API_URL;

Vue.config.productionTip = false;
Vue.component("v-selects", vSelect);
Vue.use(VuejsDialog);

const eventsHub = new Vue();
Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 720000,
});

router.beforeEach((to, from, next) => {
  // if any of the routes in ./router.js has a meta named 'requiresAuth: true'
  // then check if the user is logged in before routing to this path:
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({ name: "Login" });
    } else {
      next();
    }
  } else if (to.matched.some((record) => record.meta.requiresLogged)) {
    // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
    // then check if the user is logged in; if true continue to home page else continue routing to the destination path
    // this comes to play if the user is logged in and tries to access the login/register page
    if (store.getters.loggedIn) {
      next({ name: "Info" });
    } else {
      next();
    }
  } else {
    next();
  }
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
