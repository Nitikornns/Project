<template>
  <v-app id="app">
    <v-text-field v-model="account.email"></v-text-field>
    <v-text-field v-model="account.username"></v-text-field>
    <v-text-field v-model="account.password"></v-text-field>
    <ul v-for="account in accounts" :key="account.email">
      <td>{{ account.email }}</td>
      <td>{{ account.username }}</td>
      <td>{{ account.password }}</td>
    </ul>
    <v-btn @click="createAccounts">submit</v-btn>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "Logins",
  data() {
    return {
      account: {},
      accounts: [],
    };
  },
  async created() {
    await this.getAccount();
  },

  methods: {
    async createAccounts() {
      await axios.post("api/account/", this.account);
      console.log(this.account);
      this.account = {};
    },
    async getAccount() {
      let accounts = await axios.get("api/account/").then((r) => r.data);
      this.accounts = accounts;
    },
  },
};
</script>
