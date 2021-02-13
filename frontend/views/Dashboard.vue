<template>
  <v-app>
    <Navbar></Navbar>
    <v-dialog v-model="dialogDeleteskill" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="deleteItemConfirmSkill(skill)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogeditskill" persistent max-width="400px">
      <v-card height="320px">
        <v-card-title>
          <span class="headline">{{ formTitleEditSkill }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageeditskill }}</h6>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="skill.name"
                  :items="itemlistskill"
                  dense
                  outlined
                >
                </v-select>
              </v-col>
              <v-col cols="12">
                <v-progress-linear
                  v-model="skill.score"
                  background-color="#607D8B"
                  color="#E91E63"
                  height="30"
                  class="rounded-pill"
                >
                  <strong>{{ Math.trunc(skill.score) }}</strong>
                </v-progress-linear>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="editItemConfirmSkill(skill)"
          >
            ยืนยัน
          </v-btn>
          <v-btn color="error" depressed text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogDeleteEducation" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="deleteItemConfirmEducation(education)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogediteducation" persistent max-width="800px">
      <v-card height="490px">
        <v-card-title>
          <span class="headline">{{ formTitleEditEducation }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageediteducation }}</h6>
            <v-col cols="12">
              <v-selects v-model="education.degree" :options="educationdegree">
              </v-selects>
            </v-col>
            <v-col cols="12"
              ><v-text-field
                v-model="education.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field
            ></v-col>
            <v-col cols="12"
              ><date-picker
                v-model="education.datestart"
                valueType="format"
                name="วันเริ่ม"
                placeholder="วันเริ่ม"
              ></date-picker>
              <date-picker
                v-model="education.dateend"
                valueType="format"
                name="วันจบ"
                placeholder="วันจบ"
                class="dateend"
              ></date-picker
            ></v-col>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="editItemConfirmEducation(education)"
          >
            ยืนยัน
          </v-btn>
          <v-btn color="error" depressed text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogDeletework" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="deleteItemConfirmWork(work)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogeditwork" persistent max-width="800px">
      <v-card height="490px">
        <v-card-title>
          <span class="headline">{{ formTitleEditWork }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageeditwork }}</h6>
            <v-col cols="12">
              <v-text-field
                v-model="work.name"
                label="ชื่อ"
                outlined
                dense
              ></v-text-field>
              <v-textarea
                v-model="work.detail"
                label="รายละเอียด"
                outlined
                dense
                height="150"
              ></v-textarea>
            </v-col>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="editItemConfirmWork(work)"
          >
            ยืนยัน
          </v-btn>
          <v-btn color="error" depressed text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogDeletelanguage" persistent max-width="500px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="deleteItemConfirmLanguage(language)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogeditlanguage" persistent max-width="400px">
      <v-card height="320px">
        <v-card-title>
          <span class="headline">{{ formTitleEditLanguage }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageeditlanguage }}</h6>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="language.name"
                  :items="itemlistlanguages"
                  dense
                  outlined
                >
                </v-select>
              </v-col>
              <v-col cols="12">
                <v-progress-linear
                  v-model="language.score"
                  background-color="#607D8B"
                  color="#E91E63"
                  height="30"
                  class="rounded-pill"
                >
                  <strong>{{ Math.trunc(language.score) }}</strong>
                </v-progress-linear>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="editItemConfirmLanguage(language)"
          >
            ยืนยัน
          </v-btn>
          <v-btn color="error" depressed text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogDeleteinfo" persistent max-width="400px">
      <v-card>
        <v-card-title class="headline justify-center"
          >ต้องการจะลบใช่หรือไม่?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="deleteItemConfirmInfo(student)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogeditinfo" persistent max-width="800px">
      <v-card height="900px">
        <v-card-title>
          <span class="headline">{{ formTitleEditInfo }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 class="message">{{ messageeditinfo }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ชื่อ</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.name"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>นามสกุล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.surname"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>เลขบัตรประชาชน</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.idcard"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>อีเมล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.email"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>เบอร์โทรศัพท์</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="student.telphoneNumber"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            depressed
            text
            @click="editItemConfirmInfo(student)"
          >
            ยืนยัน
          </v-btn>
          <v-btn color="error" depressed text @click="closeEdit">
            ยกเลิก
          </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <!----------------------------- datatable ----------------------------->
    <v-card>
      <v-card-text>
        <div class="w3-display-container">
          <ul v-for="picture in pictures" :key="picture.pictureid">
            <img :src="picture.picturefile" style="width:30%" alt="Avatar" />
          </ul>
        </div>
        <div id="messages">
          {{ messages }}
        </div>
        <v-btn
          color="primary"
          dark
          class="buttonleft"
          depressed
          @click="gotoAddPicturePage"
          ><v-icon left>mdi-image</v-icon>เพิ่มรูปภาพ</v-btn
        >
        <v-btn
          color="red"
          dark
          class="buttonleft2"
          depressed
          @click="deletePicture"
          ><v-icon left>mdi-delete</v-icon>ลบรูปภาพ</v-btn
        >
      </v-card-text>
    </v-card>
    <v-container>
      <v-card>
        <v-card-text
          ><v-toolbar flat>
            <v-toolbar-title>ข้อมูลส่วนตัว</v-toolbar-title
            ><v-spacer></v-spacer>
            <v-btn
              color="primary"
              dark
              class="btn mb-2"
              depressed
              @click="gotoAddInfoPage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headersinfo"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr v-for="student in students" :key="student.id">
                  <td>{{ student.name }}</td>
                  <td>{{ student.surname }}</td>
                  <td>{{ student.idcard }}</td>
                  <td>{{ student.email }}</td>
                  <td>{{ student.telphoneNumber }}</td>
                  <v-btn
                    @click.stop="dialogeditinfo = true"
                    @click="$data.student = student"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.student = student"
                    @click.stop="dialogDeleteinfo = true"
                    color="red"
                  >
                    <v-icon small>mdi-delete</v-icon>ลบ
                  </v-btn>
                </tr>
              </tbody>
            </template>
          </v-data-table>
        </v-card-text>
        <v-card-text
          ><v-toolbar flat>
            <v-toolbar-title>ภาษา</v-toolbar-title><v-spacer></v-spacer>
            <v-btn
              color="primary"
              dark
              class="btn mb-2 buttonright"
              depressed
              @click="gotoAddLanguagePage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headerslanguage"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr v-for="language in languages" :key="language.languageid">
                  <td>{{ language.name }}</td>
                  <td>{{ language.sumscore }}</td>
                  <v-btn
                    @click.stop="dialogeditlanguage = true"
                    @click="$data.language = language"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.language = language"
                    @click.stop="dialogDeletelanguage = true"
                    color="red"
                  >
                    <v-icon small>mdi-delete</v-icon>ลบ
                  </v-btn>
                </tr>
              </tbody>
            </template>
          </v-data-table>
        </v-card-text>
        <v-card-text
          ><v-toolbar flat>
            <v-toolbar-title>การศึกษา</v-toolbar-title> <v-spacer></v-spacer>
            <v-btn color="primary" dark depressed @click="gotoAddEducationPage"
              ><v-icon> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headerseducation"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr
                  v-for="education in educations"
                  :key="education.educationid"
                >
                  <td>{{ education.degree }}</td>
                  <td>{{ education.name }}</td>
                  <td>{{ education.datestart }}</td>
                  <td>{{ education.dateend }}</td>
                  <v-btn
                    @click.stop="dialogediteducation = true"
                    @click="$data.education = education"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.education = education"
                    @click.stop="dialogDeleteEducation = true"
                    color="red"
                  >
                    <v-icon small>mdi-delete</v-icon>ลบ
                  </v-btn>
                </tr>
              </tbody>
            </template>
          </v-data-table>
        </v-card-text>
        <v-card-text
          ><v-toolbar flat>
            <v-toolbar-title>การทำงาน</v-toolbar-title><v-spacer></v-spacer
            ><v-btn color="primary" depressed dark @click="gotoAddWorkPage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headerswork"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr v-for="work in works" :key="work.workid">
                  <td>{{ work.name }}</td>
                  <td>{{ work.detail }}</td>
                  <v-btn
                    @click.stop="dialogeditwork = true"
                    @click="$data.work = work"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.work = work"
                    @click.stop="dialogDeletework = true"
                    color="red"
                  >
                    <v-icon small>mdi-delete</v-icon>ลบ
                  </v-btn>
                </tr>
              </tbody>
            </template>
          </v-data-table>
        </v-card-text>
        <v-card-text
          ><v-toolbar flat>
            <v-toolbar-title>ภาษาโปรแกรมมิ่ง</v-toolbar-title
            ><v-spacer></v-spacer
            ><v-btn color="primary" dark depressed @click="gotoAddSkillPage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headersskill"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr v-for="skill in skills" :key="skill.skillid">
                  <td>{{ skill.name }}</td>
                  <td>{{ skill.sumscore }}</td>
                  <v-btn
                    @click.stop="dialogeditskill = true"
                    @click="$data.skill = skill"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.skill = skill"
                    @click.stop="dialogDeleteskill = true"
                    color="red"
                  >
                    <v-icon small>mdi-delete</v-icon>ลบ
                  </v-btn>
                </tr>
              </tbody>
            </template>
          </v-data-table>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>
<script>
import { getAPI, axiosBase } from "../axios-api";
import { mapState } from "vuex";
import jwt_decode from "jwt-decode";
import Navbar from "../src/components/Navbar";
import "vue-select/dist/vue-select.css";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
export default {
  name: "Dashboard",
  computed: { ...mapState(["APIData"]) },
  components: { Navbar, DatePicker },
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
      picture: {},
      pictures: [],
      work: {},
      works: [],
      accountid: {},
      pictureid: {},
      formTitleEditSkill: "แก้ไขทักษะภาษาโปรแกรมมิ่ง",
      formTitleEditEducation: "แก้ไขการศึกษา",
      formTitleEditWork: "แก้ไขการทำงาน",
      formTitleEditInfo: "แก้ไขข้อมูลส่วนตัว",
      formTitleEditLanguage: "แก้ไขภาษา",
      dialogediteducation: false,
      dialogDeleteEducation: false,
      dialogeditwork: false,
      dialogDeletework: false,
      dialogeditlanguage: false,
      dialogDeletelanguage: false,
      dialogeditskill: false,
      dialogDeleteskill: false,
      dialogeditinfo: false,
      dialogDeleteinfo: false,
      messageeditinfo: "",
      messageeditskill: "",
      messageeditlanguage: "",
      messageeditwork: "",
      messageediteducation: "",
      messages: "",
      headerseducation: [
        { text: "ระดับ", align: "start", sortable: false },
        { text: "ชื่อ", sortable: false },
        { text: "วันเริ่ม", sortable: false },
        { text: "วันจบ", sortable: false },
      ],
      headersinfo: [
        { text: "ชื่อ", sortable: false },
        { text: "นามสกุล", sortable: false },
        { text: "รหัสบัตรประชาชน", sortable: false },
        { text: "อีเมล", sortable: false },
        { text: "หมายเลขโทรศัพท์", sortable: false },
      ],
      headerslanguage: [
        { text: "ภาษา", align: "start", sortable: false },
        { text: "ระดับความถนัด", sortable: false },
      ],
      headersskill: [
        { text: "ภาษา", align: "start", sortable: false },
        { text: "ระดับความถนัด", sortable: false },
      ],
      headerswork: [
        { text: "ชื่อ", align: "start", sortable: false },
        { text: "รายละเอียด", sortable: false },
      ],
      educationdegree: [
        "มัธยมศึกษา",
        "ประกาศนียบัตรวิชาชีพ (ปวช.)",
        "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)",
        "ปริญญาตรี",
        "ปริญญาโท",
        "ปริญญาเอก",
      ],
      itemlistlanguages: [
        "กัมพูชา",
        "กาตาร์",
        "เกาหลีใต้",
        "เกาหลีเหนือ",
        "คาซัคสถาน",
        "คีร์กีซสถาน",
        "คูเวต",
        "จอร์เจีย",
        "จอร์แดน",
        "จีน",
        "ซาอุดีอาระเบีย",
        "ซีเรีย",
        "ไซปรัส",
        "ญี่ปุ่น",
        "ติมอร์ตะวันออกติมอร์-เลสเต",
        "ตุรกี",
        "เติร์กเมนิสถาน",
        "ไต้หวัน",
        "ทาจิกิสถาน",
        "ไทย",
        "เนปาล",
        "บรูไน",
        "บังกลาเทศ",
        "บาห์เรน",
        "ปากีสถาน",
        "ปาเลสไตน์",
        "ฝรั่งเศษ",
        "พม่าเมียนมา",
        "ฟิลิปปินส์",
        "ภูฏาน",
        "มองโกเลีย",
        "มัลดีฟส์",
        "มาเลเซีย",
        "เยเมน",
        "ลาว",
        "เลบานอน",
        "เวียดนาม",
        "ศรีลังกา",
        "สหรัฐอาหรับเอมิเรตส์",
        "สิงคโปร์",
        "อัฟกานิสถาน",
        "อาเซอร์ไบจาน",
        "อาร์มีเนีย",
        "อินเดีย",
        "อินโดนีเซีย",
        "อิรัก",
        "อิสราเอล",
        "อิหร่าน",
        "อุซเบกิสถาน",
        "โอมาน",
        "อังกฤษ",
      ],
      itemlistskill: ["Java", "Python", "Html", "C", "JavaScript", "C++", "C#"],
    };
  },
  created() {
    this.getAPIData();
    this.setFormData();
  },
  methods: {
    getSuccessEditMessage() {
      let message = "แก้ไขสำเร็จ";
      let options = {
        okText: "ปิด",
        cancelText: "Cancel",
        animation: "bounce",
        type: "basic",
      };
      this.$dialog.alert(message, options);
    },
    getSuccessDeleteMessage() {
      let message = "ลบสำเร็จ";
      let options = {
        okText: "ปิด",
        cancelText: "Cancel",
        animation: "bounce",
        type: "basic",
      };
      this.$dialog.alert(message, options);
    },
    getFailedEditMessage() {
      this.messageeditinfo = "กรอกข้อมูลให้ถูกต้องตามรูปแบบให้ครบถ้วน";
      this.messageediteducation = "กรอกข้อมูลให้ถูกต้องตามรูปแบบให้ครบถ้วน";
    },
    setFormData() {
      this.work = {};
      this.language = { score: 0 };
      this.student = {};
      this.education = {};
      this.skill = { score: 0 };
      this.picture = {};
      this.messages = "";
      this.messageeditinfo = "";
      this.messageeditskill = "";
      this.messageeditlanguage = "";
      this.messageeditwork = "";
      this.messageediteducation = "";
    },
    closeDelete() {
      this.getAPIData();
      this.dialogDeleteskill = false;
      this.dialogDeleteEducation = false;
      this.dialogDeletework = false;
      this.dialogDeleteinfo = false;
      this.dialogDeletelanguage = false;
    },
    closeEdit() {
      this.getAPIData();
      this.dialogeditskill = false;
      this.dialogediteducation = false;
      this.dialogeditwork = false;
      this.dialogeditlanguage = false;
      this.dialogeditinfo = false;
      this.setFormData();
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
        .get("/api/students/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.students = this.$store.state.APIData;
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
    async getAccountid() {
      let token = localStorage.getItem("access_token");
      let decoded = jwt_decode(token);
      await getAPI
        .get("/accounts/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.accountid = decoded.user_id;
          return this.accountid;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteItemConfirmSkill(skill) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/skills/${skill.skillid}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.closeDelete();
          this.setFormData();
          this.getSuccessDeleteMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async editItemConfirmSkill(skill) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/skills/${skill.skillid}/`,
          {
            accountid: this.accountid,
            skillid: this.skill.skillid,
            name: this.skill.name,
            score: this.skill.score,
            sumscore: this.skill.sumscore,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.closeEdit();
          this.setFormData();
          this.getSuccessEditMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteItemConfirmWork(work) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/works/${work.workid}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.closeDelete();
          this.setFormData();
          this.getSuccessDeleteMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async editItemConfirmWork(work) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/works/${work.workid}/`,
          {
            accountid: this.accountid,
            workid: this.work.workid,
            name: this.work.name,
            detail: this.work.detail,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.closeEdit();
          this.setFormData();
          this.getSuccessEditMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteItemConfirmLanguage(language) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/languages/${language.languageid}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.closeDelete();
          this.setFormData();
          this.getSuccessDeleteMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async editItemConfirmLanguage(language) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/languages/${language.languageid}/`,
          {
            accountid: this.accountid,
            languageid: this.language.languageid,
            name: this.language.name,
            score: this.language.score,
            sumscore: this.language.sumscore,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.closeEdit();
          this.setFormData();
          this.getSuccessEditMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteItemConfirmInfo(student) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/students/${student.studentid}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.closeDelete();
          this.setFormData();
          this.getSuccessDeleteMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async editItemConfirmInfo(student) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/students/${student.studentid}/`,
          {
            accountid: this.accountid,
            name: this.student.name,
            surname: this.student.surname,
            idcard: this.student.idcard,
            email: this.student.email,
            telphoneNumber: this.student.telphoneNumber,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.closeEdit();
          this.setFormData();
          this.getSuccessEditMessage();
        })
        .catch((err) => {
          console.log(err);
          this.getFailedEditMessage();
        });
    },
    async deleteItemConfirmEducation(education) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/educations/${education.educationid}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.closeDelete();
          this.setFormData();
          this.getSuccessDeleteMessage();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async editItemConfirmEducation(education) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/educations/${education.educationid}/`,
          {
            accountid: this.accountid,
            educationid: this.education.educationid,
            datestart: this.education.datestart,
            dateend: this.education.dateend,
            name: this.education.name,
            degree: this.education.degree,
          },
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
          }
        )
        .then(() => {
          this.closeEdit();
          this.setFormData();
          this.getSuccessEditMessage();
        })
        .catch((err) => {
          console.log(err);
          this.getFailedEditMessage();
        });
    },
    async getPictureid() {
      await getAPI
        .get("/api/pictures/", {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((response) => {
          this.$store.state.APIData = response.data;
          this.pictureid = response.data;
          return this.pictureid;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deletePicture() {
      await this.getPictureid();
      await axiosBase
        .delete(`api/pictures/${this.pictureid[0].pictureid}/`, {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then(() => {
          this.setFormData();
          this.successDeleteMessage();
          this.fetchStatusMessage();
          this.getAPIData();
        })
        .catch((err) => {
          console.log(err);
          console.log(this.pictureid[0].pictureid);
        });
    },
    fetchStatusMessage() {
      setInterval(this.setStatusMessage, 5000);
    },
    setStatusMessage() {
      this.messages = "";
    },
    successDeleteMessage() {
      document.getElementById("messages").style.color = "green";
      this.message = "ลบรูปภาพสำเร็จ";
    },
    gotoAddEducationPage() {
      this.$router.push({ name: "Education" });
    },
    gotoAddSkillPage() {
      this.$router.push({ name: "Skill" });
    },
    gotoAddLanguagePage() {
      this.$router.push({ name: "Language" });
    },
    gotoAddWorkPage() {
      this.$router.push({ name: "Work" });
    },
    gotoAddInfoPage() {
      this.$router.push({ name: "Info" });
    },
    gotoAddPicturePage() {
      this.$router.push({ name: "Picture" });
    },
  },
};
</script>
