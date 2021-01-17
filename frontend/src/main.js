import Vue from "vue";
import App from "./App.vue";
import router from "../Router";

import vuetify from "@/plugins/vuetify";

import axios from "axios";

import vSelect from "vue-select";

axios.defaults.baseURL = process.env.VUE_APP_API_URL;

Vue.config.productionTip = false;
Vue.component("v-selects", vSelect);

new Vue({
  router,
  render: (h) => h(App),
  vuetify,
}).$mount("#app");
