<template>
  <v-app>
    <button @click="generateReport">ดาวโหลดpdf</button>
    <vue-html2pdf
      :show-layout="false"
      :float-layout="true"
      :enable-download="true"
      :preview-modal="true"
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

          <body class="w3-light-grey">
            <!-- Page Container -->
            <div class="w3-content w3-margin-top" style="max-width:1400px;">
              <!-- The Grid -->
              <div class="w3-row-padding">
                <!-- Left Column -->
                <div class="w3-third">
                  <div class="w3-white w3-text-grey w3-card-4">
                    <div class="w3-display-container">
                      <!--<img
                        src="/w3images/avatar_hat.jpg"
                        style="width:100%"
                        alt="Avatar"
                      />-->

                      <div
                        class="w3-display-bottomleft w3-container w3-text-black"
                      >
                        <h2 v-for="student in students" :key="student.name">
                          {{ student.name }}
                        </h2>
                      </div>
                    </div>

                    <div class="w3-container">
                      <p v-for="student in students" :key="student.name">
                        <i
                          class="fa fa-user fa-fw w3-margin-right w3-large w3-text-teal"
                        ></i
                        >{{ student.name }} {{ student.surname }}
                      </p>

                      <p v-for="student in students" :key="student.email">
                        <i
                          class="fa fa-envelope fa-fw w3-margin-right w3-large w3-text-teal"
                        ></i
                        >{{ student.email }}
                      </p>

                      <p
                        v-for="student in students"
                        :key="student.telphoneNumber"
                      >
                        <i
                          class="fa fa-phone fa-fw w3-margin-right w3-large w3-text-teal"
                        ></i
                        >{{ student.telphoneNumber }}
                      </p>

                      <hr />

                      <p class="w3-mediam">
                        <b
                          ><i
                            class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                          ></i
                          >ภาษาโปรแกรมมิ่ง</b
                        >
                      </p>

                      <ul v-for="skill in skills" :key="skill.name">
                        {{
                          skill.name
                        }}

                        <div>
                          <v-progress-linear
                            class="w3-round-xlarge"
                            v-model="skill.score"
                            background-color="w3-light-grey"
                            color="#009383"
                            height="19"
                          >
                            <td style="text-align:center;font-size:12px">
                              <strong>{{ Math.trunc(skill.score) }}%</strong>
                            </td>
                          </v-progress-linear>
                        </div>
                      </ul>
                      <br />
                      <p class="w3-mediam">
                        <b
                          ><i
                            class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                          ></i
                          >ภาษา</b
                        >
                      </p>
                      <ul v-for="language in languages" :key="language.name">
                        {{
                          language.name
                        }}

                        <div class="w3-light-grey w3-round-xlarge">
                          <div>
                            <v-progress-linear
                              class="w3-round-xlarge"
                              v-model="language.score"
                              background-color="w3-light-grey"
                              color="#009383"
                              height="19"
                              ><td style="text-align:center;font-size:12px">
                                <strong
                                  >{{ Math.trunc(language.score) }}%</strong
                                >
                              </td>
                            </v-progress-linear>
                          </div>
                        </div>
                      </ul>
                      <br />
                    </div>
                  </div>
                  <br />

                  <!-- End Left Column -->
                </div>

                <!-- Right Column -->
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
                        <b>{{ education.schoolname }}</b>
                      </h5>
                      <h6 class="w3-text-teal">
                        <i class="fa fa-calendar fa-fw w3-margin-right"></i>
                        {{ education.datestart }} - {{ education.dateend }}
                      </h6>
                      <p>
                        {{ education.detail }}
                      </p>
                      <hr />
                    </div>
                  </div>

                  <div class="w3-container w3-card w3-white">
                    <h2 class="w3-text-grey w3-padding-16">
                      <i
                        class="fa fa-certificate fa-fw w3-margin-right w3-xxlarge w3-text-teal"
                      ></i
                      >work
                    </h2>
                    <div class="w3-container">
                      <h5 class="w3-opacity"><b>W3Schools.com</b></h5>
                      <h6 class="w3-text-teal">
                        <i class="fa fa-calendar fa-fw w3-margin-right"></i
                        >Forever
                      </h6>
                      <p>Web Development! All I need to know in one place</p>
                      <hr />
                    </div>
                    <div class="w3-container">
                      <h5 class="w3-opacity"><b>London Business School</b></h5>
                      <h6 class="w3-text-teal">
                        <i class="fa fa-calendar fa-fw w3-margin-right"></i>2013
                        - 2015
                      </h6>
                      <p>Master Degree</p>
                      <hr />
                    </div>
                    <div class="w3-container">
                      <h5 class="w3-opacity"><b>School of Coding</b></h5>
                      <h6 class="w3-text-teal">
                        <i class="fa fa-calendar fa-fw w3-margin-right"></i>2010
                        - 2013
                      </h6>
                      <p>Bachelor Degree</p>
                      <br />
                    </div>
                  </div>

                  <!-- End Right Column -->
                </div>

                <!-- End Grid -->
              </div>

              <!-- End Page Container -->
            </div>

            <footer class="w3-container w3-teal w3-center w3-margin-top">
              <p>Find me on social media.</p>
              <i class="fa fa-facebook-official w3-hover-opacity"></i>
              <i class="fa fa-instagram w3-hover-opacity"></i>
              <i class="fa fa-snapchat w3-hover-opacity"></i>
              <i class="fa fa-pinterest-p w3-hover-opacity"></i>
              <i class="fa fa-twitter w3-hover-opacity"></i>
              <i class="fa fa-linkedin w3-hover-opacity"></i>
              <p>
                Powered by
                <a
                  href="https://www.w3schools.com/w3css/default.asp"
                  target="_blank"
                  >w3.css</a
                >
              </p>
            </footer>
          </body>
        </html>
      </section>
    </vue-html2pdf>
  </v-app>
</template>

<script>
import axios from "axios";
import VueHtml2pdf from "vue-html2pdf";
export default {
  name: "Pdf",
  components: {
    VueHtml2pdf,
  },
  data() {
    return {
      student: {},
      students: [],
      skill: {},
      skills: [],
      language: {},
      languages: [],
      education: {},
      educations: [],
    };
  },
  async created() {
    await this.getStudent();
    await this.getSkill();
    await this.getLanguage();
    await this.getEducation();
  },
  methods: {
    generateReport() {
      this.$refs.html2Pdf.generatePdf();
    },
    async getStudent() {
      let students = await axios.get("api/students/").then((r) => r.data);
      this.students = students;
    },
    async getSkill() {
      let skills = await axios.get("api/skills/").then((r) => r.data);
      this.skills = skills;
    },
    async getLanguage() {
      let languages = await axios.get("api/languages/").then((r) => r.data);
      this.languages = languages;
    },
    async getEducation() {
      let educations = await axios.get("api/educations/").then((r) => r.data);
      this.educations = educations;
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
</style>
