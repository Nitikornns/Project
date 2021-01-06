import Vue from "vue";
import App from "./App.vue";
import router from "../Router";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import axios from 'axios'

axios.defaults.baseURL = process.env.VUE_APP_API_URL;

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

Vue.use(BootstrapVue);
