import Vue from "vue";
import App from "./App.vue";
import router from "../Router";
import axios from "axios";
import vSelect from "vue-select";
import VuejsDialog from "vuejs-dialog";
import "vuejs-dialog/dist/vuejs-dialog.min.css";
import store from "../store.js";
import vuetify from "@/plugins/vuetify";

axios.defaults.baseURL = process.env.VUE_APP_API_URL;

Vue.config.productionTip = false;
Vue.component("v-selects", vSelect);
Vue.use(VuejsDialog);

router.beforeEach((to, form, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: "Login" });
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
