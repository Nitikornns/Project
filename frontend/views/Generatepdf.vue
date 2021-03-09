<template>
  <v-app>
    <Navbar></Navbar>
    <v-card class="container">
      <v-card-text>
        <v-btn color="blue" height="100" width="600" @click="generateFilePdf"
          ><v-icon>mdi-file-pdf</v-icon>ดาวโหลด</v-btn
        ></v-card-text
      >
      <v-btn @click="gotoPreviuosPage" color="primary" depressed>ย้อนกลับ</v-btn
      >{{ info.address }}
    </v-card>
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="true"
      :paginate-elements-by-height="1400"
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
          <body>
            <!-- Page Container -->
            <div class="w3-content w3-margin-top" style="max-width:1400px;">
              <!-- The Grid -->
              <div class="w3-row-padding">
                <!-- Left Column -->
                <div class="w3-third">
                  <div
                    class="w3-white w3-text-grey w3-card-4"
                    id="box"
                    style="width:240px;"
                  >
                    <div class="w3-display-container">
                      <ul v-for="picture in pictures" :key="picture.pictureid">
                        <img
                          :src="picture.picturefile"
                          style="width:100%"
                          alt="Avatar"
                        />
                      </ul>
                    </div>
                    <div class="container">
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
                      <ul v-if="info.address != null">
                        <p v-for="info in infos" :key="info.address">
                          <i
                            class="fa fa-home fa-fw w3-margin-right w3-large w3-text-teal"
                          ></i
                          >{{ info.address }}
                        </p>
                      </ul>
                    </div>
                    <hr />
                    <div class="w3-container">
                      <div v-if="skills.length >= 1">
                        <i
                          class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                        ></i
                        >ทักษะ
                        <div v-for="skill in skills" :key="skill.name">
                          <div class="w3-container">
                            {{ skill.name }} : {{ skill.detail }}
                          </div>
                        </div>
                      </div>
                    </div>
                    <hr />
                    <div class="w3-container">
                      <div v-if="talents.length >= 1">
                        <i
                          class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                        ></i
                        >ความสามารถพิเศษ
                        <div v-for="talent in talents" :key="talent.name">
                          <div class="w3-container">
                            {{ talent.name }} : {{ talent.detail }}
                          </div>
                        </div>
                      </div>
                    </div>
                    <hr />
                    <div class="w3-container">
                      <div v-if="hobbies.length >= 1">
                        <i
                          class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                        ></i
                        >งานอดิเรก
                        <div v-for="hobby in hobbies" :key="hobby.name">
                          <div class="w3-container">{{ hobby.name }}</div>
                        </div>
                      </div>
                    </div>
                    <hr />
                  </div>
                  <!-- End Left Column -->
                </div>
                <!-- Right Column -->
                <div class="w3-twothird">
                  <div
                    class="w3-container w3-card w3-white w3-margin-bottom"
                    id="box"
                  >
                    <h2 class="w3-text-grey w3-padding-16">
                      <i
                        class="fa fa-graduation-cap fa-fw w3-margin-right w3-xxlarge w3-text-teal"
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
                      {{ education.name }}
                      <h6 class="w3-text-teal">
                        <ul v-if="education.dateend != null">
                          <i class="fa fa-calendar fa-fw w3-margin-right"></i>
                          {{
                            education.datestart
                          }}
                          -
                          {{
                            education.dateend
                          }}
                        </ul>
                        <ul v-if="education.dateend == null">
                          <i class="fa fa-calendar fa-fw w3-margin-right"></i>
                          {{
                            education.datestart
                          }}
                          - ปัจจุบัน
                        </ul>
                      </h6>
                    </div>
                  </div>
                  <div
                    class="w3-container w3-card w3-white w3-margin-bottom"
                    id="box"
                  >
                    <h2 class="w3-text-grey w3-padding-16">
                      <i
                        class="fa fa-briefcase fa-fw w3-margin-right w3-xxlarge w3-text-teal"
                      ></i
                      >ประสบการณ์การทำงาน
                    </h2>
                    <div
                      class="w3-container"
                      v-for="experience in experiences"
                      :key="experience.experienceid"
                    >
                      <h5 class="w3-opacity">
                        <b>{{ experience.name }}</b>
                      </h5>
                      <h6 class="w3-text-teal">
                        <ul v-if="experience.dateend != null">
                          <i class="fa fa-calendar fa-fw w3-margin-right"></i>
                          {{
                            experience.datestart
                          }}
                          -
                          {{
                            experience.dateend
                          }}
                        </ul>
                        <ul v-if="experience.dateend == null">
                          <i class="fa fa-calendar fa-fw w3-margin-right"></i>
                          {{
                            experience.datestart
                          }}
                          - ปัจจุบัน
                        </ul>
                      </h6>
                      <div class="w3-container">{{ experience.detail }}</div>
                    </div>
                  </div>
                  <div
                    class="w3-container w3-card w3-white w3-margin-bottom"
                    id="box"
                  >
                    <h2 class="w3-text-grey w3-padding-16">
                      <i
                        class="fa fa-trophy fa-fw w3-margin-right w3-xxlarge w3-text-teal"
                      ></i
                      >ผลงาน
                    </h2>
                    <div
                      class="w3-container"
                      v-for="work in works"
                      :key="work.workid"
                    >
                      <h5 class="w3-opacity">
                        <b>{{ work.name }}</b>
                      </h5>
                      <div class="w3-container">{{ work.detail }}</div>
                    </div>
                  </div>
                </div>
                <!-- End Right Column -->
              </div>
              <!-- End Grid -->
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
      work: {},
      works: [],
      education: {},
      educations: [],
      picture: {},
      pictures: [],
      experience: {},
      experiences: [],
      talent: {},
      talents: [],
      hobby: {},
      hobbies: [],
    };
  },
  async created() {
    await this.getAPIData();
  },
  methods: {
    async generateFilePdf() {
      await this.getAPIData();
      this.$refs.html2Pdf.generatePdf();
    },
    async getAPIData() {
      await getAPI
        .get("/api/experiences/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.experiences = this.$store.state.APIData;
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
        .get("/api/hobbies/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.hobbies = this.$store.state.APIData;
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
        .get("/api/talents/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.talents = this.$store.state.APIData;
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
img {
  border: 5px solid #555;
}
#box {
  border: 1px solid;
  padding: 10px;
  box-shadow: 5px 10px 18px #888888;
}
</style>
