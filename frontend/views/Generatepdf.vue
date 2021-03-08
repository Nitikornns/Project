<template>
  <v-app>
    <Navbar></Navbar>
    <v-card class="container">
      <v-card-text>
        <v-btn color="blue" height="100" width="600" @click="generateFilePdf"
          ><v-icon>mdi-file-pdf</v-icon>ดาวโหลด</v-btn
        ></v-card-text
      >
      <ul v-if="work == null">
        have
      </ul>
      <div v-if="works.length == 1">
        have
      </div>
      <v-btn @click="gotoPreviuosPage" color="primary" depressed
        >ย้อนกลับ</v-btn
      >
    </v-card>
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="true"
      :paginate-elements-by-height="2000"
      filename="MyCV"
      :pdf-quality="2"
      :manual-pagination="false"
      pdf-format="a4"
      pdf-orientation="portrait"
      pdf-content-width="800px"
      ref="html2Pdf"
    >
      <section slot="pdf-content">
        <html>
          <title>W3.CSS Template</title>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <link
            rel="stylesheet"
            href="https://www.w3schools.com/w3css/4/w3.css"
          />
          <link
            rel="stylesheet"
            href="https://fonts.googleapis.com/css?family=Roboto"
          />
          <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
          />
          <body class="w3-light-grey">
            <!-- Page Container -->
            <div class="w3-content w3-margin-top" style="max-width:1400px;">
              <!-- The Grid -->
              <div class="w3-row-padding">
                <!-- Left Column -->
                <div class="w3-third">
                  <div class="w3-white w3-text-grey w3-card-4">
                    <div class="w3-display-container">
                      <ul v-for="picture in pictures" :key="picture.pictureid">
                        <img
                          :src="picture.picturefile"
                          style="width:100%"
                          alt="Avatar"
                        />
                      </ul>
                    </div>
                    <div class="w3-container">
                      <p v-for="info in infos" :key="info.name">
                        <i
                          class="fa fa-user fa-fw w3-margin-right w3-large w3-text-teal"
                        ></i
                        >{{ info.name }} {{ info.surname }}
                      </p>
                      <p v-for="info in infos" :key="info.email">
                        <i
                          class="fa fa-envelope fa-fw w3-margin-right w3-large w3-text-teal"
                        ></i
                        >{{ info.email }}
                      </p>
                      <p v-for="info in infos" :key="info.telphoneNumber">
                        <i
                          class="fa fa-phone fa-fw w3-margin-right w3-large w3-text-teal"
                        ></i
                        >{{ info.telphoneNumber }}
                      </p>
                      <hr />
                      <div v-if="skill.length >= 1">
                        <p class="w3-mediam">
                          <b
                            ><i
                              class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                            ></i
                            >ภาษาโปรแกรมมิ่ง</b
                          >
                        </p>
                        <ul v-for="skill in skills" :key="skill.name">
                          <div class="w3-container">
                            {{ skill.name }}
                            <div>{{ skill.degree }}</div>
                          </div>
                        </ul>
                      </div>
                      <br />
                      <div v-if="language.length >= 1">
                        <p class="w3-mediam">
                          <b
                            ><i
                              class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                            ></i
                            >ภาษา</b
                          >
                        </p>
                        <ul v-for="language in languages" :key="language.name">
                          <div class="w3-container">
                            {{ language.name }}
                            <div>{{ language.degree }}</div>
                          </div>
                        </ul>
                      </div>
                      <br />
                    </div>
                  </div>
                  <br />
                  <!-- End Left Column -->
                </div>
                <!-- Right Column -->
                <div v-if="education.length >= 1">
                  <div class="w3-twothird">
                    <div class="w3-container w3-card w3-white w3-margin-bottom">
                      <h2 class="w3-text-grey w3-padding-16">
                        <i
                          class="fa fa-certificate fa-fw w3-margin-right w3-xxlarge w3-text-teal"
                        ></i
                        >การศึกษา
                      </h2>
                      <div
                        class="w3-container"
                        v-for="education in educations"
                        :key="education.educationid"
                      >
                        <h5 class="w3-opacity">
                          <b>{{ education.degree }}</b>
                        </h5>
                        <h6 class="w3-text-teal">
                          <i class="fa fa-calendar fa-fw w3-margin-right"></i>
                          {{ education.datestart }} - {{ education.dateend }}
                        </h6>
                        <p>{{ education.name }}</p>
                        <hr />
                      </div>
                    </div>
                  </div>
                  <div v-if="works.length >= 1">
                    <div class="w3-container w3-card w3-white">
                      <h2 class="w3-text-grey w3-padding-16">
                        <i
                          class="fa fa-suitcase fa-fw w3-margin-right w3-xxlarge w3-text-teal"
                        ></i
                        >การทำงาน
                      </h2>
                      <ul v-for="work in works" :key="work.workid">
                        <div class="w3-container">
                          <h5 class="w3-opacity">
                            <b>{{ work.name }}</b>
                          </h5>
                          <p>{{ work.detail }}</p>
                          <hr />
                        </div>
                      </ul>
                    </div>
                  </div>
                  <!-- End Right Column -->
                </div>
                <!-- End Grid -->
              </div>
              <!-- End Page Container -->
            </div>
            <footer
              class="w3-container w3-teal w3-center w3-margin-top"
            ></footer>
          </body>
        </html>
      </section>
    </vue-html2pdf>
  </v-app>
</template>
<script>
import Navbar from "../src/components/Navbar";
import VueHtml2pdf from "vue-html2pdf";
import { getAPI } from "../axios-api";
import { mapState } from "vuex";
export default {
  name: "Generatepdf",
  components: { VueHtml2pdf, Navbar },
  computed: { ...mapState(["APIData"]) },
  data() {
    return {
      info: {},
      infos: [],
      skill: {},
      skills: [],
      language: {},
      languages: [],
      education: {},
      educations: [],
      picture: {},
      pictures: [],
      work: {},
      works: [],
    };
  },
  created() {
    this.getAPIData();
  },
  methods: {
    async generateFilePdf() {
      await this.getAPIData();
      this.$refs.html2Pdf.generatePdf();
    },
    async getAPIData() {
      await getAPI
        .get("/api/works/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.works = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
      await getAPI
        .get("/api/educations/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.educations = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
      await getAPI
        .get("/api/skills/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.skills = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
      await getAPI
        .get("/api/infos/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.infos = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
      await getAPI
        .get("/api/languages/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.languages = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
      await getAPI
        .get("/api/pictures/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.pictures = this.$store.state.APIData;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    gotoPreviuosPage() {
      this.$router.push({ name: "Dashboard" });
    },
  },
};
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
html,
body,
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Roboto", sans-serif;
}
</style>
