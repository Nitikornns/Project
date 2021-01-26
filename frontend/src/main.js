import Vue from "vue";
import App from "./App.vue";
import router from "../Router";
import vuetify from "@/plugins/vuetify";
import axios from "axios";
import vSelect from "vue-select";
import VuejsDialog from 'vuejs-dialog';
import 'vuejs-dialog/dist/vuejs-dialog.min.css';
axios.defaults.baseURL = process.env.VUE_APP_API_URL;
Vue.config.productionTip = false;
Vue.component("v-selects", vSelect);
Vue.use(VuejsDialog);
new Vue({
 router,
 render: (h) => h(App),
 vuetify,
}).$mount("#app");
