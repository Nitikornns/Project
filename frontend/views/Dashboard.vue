<template>
  <v-app>
    <Navbar></Navbar>
    <v-dialog v-model="dialogDeletepicture" persistent max-width="500px">
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
            @click="deleteItemConfirmPicture()"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
    <v-dialog v-model="dialogDeletehobby" persistent max-width="500px">
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
            @click="deleteItemConfirmHobby(hobby)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogedithobby" persistent max-width="620px">
      <v-card height="320px">
        <v-card-title>
          <span class="headline">{{ formTitleEditHobby }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 id="message">{{ messageedithobby }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>งานอดิเรก</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="hobby.name"
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
            @click="editItemConfirmHobby(hobby)"
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
    <v-dialog v-model="dialogeditwork" persistent max-width="620px">
      <v-card height="340px">
        <v-card-title>
          <span class="headline">{{ formTitleEditWork }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 id="message">{{ messageeditwork }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ผลงาน</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field v-model="work.name" outlined dense></v-text-field>
              </v-col>
            </v-row>
            <br />
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>รายอะเอียด</v-subheader> </v-col>
              <v-col cols="7"
                ><v-text-field
                  v-model="work.detail"
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

    <v-dialog v-model="dialogeditskill" persistent max-width="620px">
      <v-card height="350px">
        <v-card-title>
          <span class="headline">{{ formTitleEditSkill }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 id="message">{{ messageeditskill }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ทักษะด้าน</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="skill.name"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>รายละเอียด</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="skill.detail"
                  outlined
                  dense
                ></v-text-field
              ></v-col>
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
            <h6 id="message">{{ messageediteducation }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ระดับ</v-subheader>
              </v-col>
              <v-col cols="7"
                ><v-selects
                  v-model="education.degree"
                  :options="educationdegree"
                >
                </v-selects>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>สถานศึกษา</v-subheader></v-col>
              <v-col cols="7"
                ><v-text-field
                  v-model="education.name"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ปีที่เข้าศึกษา</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-selects v-model="education.datestart" :options="years">
                </v-selects>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ปีที่จบการศึกษา</v-subheader></v-col
              >
              <v-col cols="7">
                <v-selects v-model="education.dateend" :options="years">
                </v-selects>
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
    <v-dialog v-model="dialogDeleteexperience" persistent max-width="500px">
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
            @click="deleteItemConfirmExperience(experience)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogeditexperience" persistent max-width="850px">
      <v-card height="590px">
        <v-card-title>
          <span class="headline">{{ formTitleEditExperience }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 id="message">{{ messageeditexperience }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>งาน</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="experience.name"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ปีที่เริ่มเข้าทำงาน</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-selects v-model="experience.datestart" :options="years">
                </v-selects>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ปีที่จบจากงาน</v-subheader></v-col>
              <v-col cols="7">
                <v-selects v-model="experience.dateend" :options="years">
                </v-selects>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>รายละเอียด</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-textarea
                  v-model="experience.detail"
                  outlined
                  dense
                  height="150"
                ></v-textarea>
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
            @click="editItemConfirmExperience(experience)"
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
    <v-dialog v-model="dialogDeletetalent" persistent max-width="500px">
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
            @click="deleteItemConfirmTalent(talent)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogedittalent" persistent width="700px">
      <v-card height="380px">
        <v-card-title>
          <span class="headline">{{ formTitleEditTalent }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 id="message">{{ messageedittalent }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3">
                <v-subheader>ความสามารถด้าน</v-subheader>
              </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="talent.name"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>รายอะเอียด</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="talent.detail"
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
            @click="editItemConfirmTalent(talent)"
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
            @click="deleteItemConfirmInfo(info)"
            >ยืนยัน</v-btn
          >
          <v-btn color="error" depressed text @click="closeDelete">ยกเลิก</v-btn
          ><v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogeditinfo" persistent max-width="800px">
      <v-card height="570px">
        <v-card-title>
          <span class="headline">{{ formTitleEditInfo }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <h6 id="message">{{ messageeditinfo }}</h6>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ชื่อ</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field v-model="info.name" outlined dense></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>นามสกุล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="info.surname"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>อีเมล</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="info.email"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>เบอร์โทรศัพท์</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="info.telphoneNumber"
                  outlined
                  dense
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row align="center" justify="center">
              <v-col cols="3"> <v-subheader>ที่อยู่</v-subheader> </v-col>
              <v-col cols="7">
                <v-text-field
                  v-model="info.address"
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
            @click="editItemConfirmInfo(info)"
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
    <v-card> </v-card>
    <v-container>
      <v-card>
        <v-card-text>
          <v-toolbar flat
            ><v-toolbar-title>รูปภาพ</v-toolbar-title><v-spacer></v-spacer
            ><v-btn
              color="primary"
              dark
              class="btn mb-2"
              depressed
              @click="gotoAddPicturePage"
              ><v-icon left>mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <div class="w3-display-container">
            <tr v-for="picture in pictures" :key="picture.pictureid">
              <td>
                <img
                  :src="picture.picturefile"
                  style="width:30%"
                  alt="Avatar"
                />
              </td>
              <td>
                <v-btn
                  color="red"
                  class="buttonleft"
                  @click="$data.picture = picture"
                  @click.stop="dialogDeletepicture = true"
                  ><v-icon left>mdi-delete</v-icon>ลบ</v-btn
                >
              </td>
            </tr>
          </div>
        </v-card-text>
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
                <tr v-for="info in infos" :key="info.id">
                  <td>{{ info.name }}</td>
                  <td>{{ info.surname }}</td>
                  <td>{{ info.email }}</td>
                  <td>{{ info.telphoneNumber }}</td>
                  <td>{{ info.address }}</td>
                  <v-btn
                    @click.stop="dialogeditinfo = true"
                    @click="$data.info = info"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.info = info"
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
            <v-toolbar-title>ผลงาน</v-toolbar-title><v-spacer></v-spacer>
            <v-btn
              color="primary"
              dark
              class="btn mb-2"
              depressed
              @click="gotoAddWorkPage"
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
                <tr v-for="work in works" :key="work.id">
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
            <v-toolbar-title>ความสามารถพิเศษ</v-toolbar-title
            ><v-spacer></v-spacer>
            <v-btn
              color="primary"
              dark
              class="btn mb-2 buttonright"
              depressed
              @click="gotoAddTalentPage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headerstalent"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr v-for="talent in talents" :key="talent.talentid">
                  <td>{{ talent.name }}</td>
                  <td>{{ talent.detail }}</td>
                  <v-btn
                    @click.stop="dialogedittalent = true"
                    @click="$data.talent = talent"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.talent = talent"
                    @click.stop="dialogDeletetalent = true"
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
            <v-toolbar-title>ประสบการณ์การทำงาน</v-toolbar-title
            ><v-spacer></v-spacer
            ><v-btn
              color="primary"
              depressed
              dark
              @click="gotoAddExperiencePage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headersexperience"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr
                  v-for="experience in experiences"
                  :key="experience.experienceid"
                >
                  <td>{{ experience.name }}</td>
                  <td>{{ experience.datestart }}</td>
                  <td>{{ experience.dateend }}</td>
                  <td>{{ experience.detail }}</td>
                  <v-btn
                    @click.stop="dialogeditexperience = true"
                    @click="$data.experience = experience"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.experience = experience"
                    @click.stop="dialogDeleteexperience = true"
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
            <v-toolbar-title>ทักษะ</v-toolbar-title><v-spacer></v-spacer
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
                  <td>{{ skill.detail }}</td>
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
        <v-card-text
          ><v-toolbar flat>
            <v-toolbar-title>งานอดิเรก</v-toolbar-title><v-spacer></v-spacer
            ><v-btn color="primary" dark depressed @click="gotoAddHobbyPage"
              ><v-icon left> mdi-plus-thick</v-icon>เพิ่ม</v-btn
            >
          </v-toolbar>
          <v-data-table
            :headers="headershobby"
            class="elevation-1"
            hide-default-footer
          >
            <template v-slot:body>
              <tbody>
                <tr v-for="hobby in hobbies" :key="hobby.hobbyid">
                  <td>{{ hobby.name }}</td>
                  <v-btn
                    @click.stop="dialogedithobby = true"
                    @click="$data.hobby = hobby"
                    color="success"
                  >
                    <v-icon small>mdi-pencil</v-icon>แก้ไข
                  </v-btn>
                  <v-btn
                    @click="$data.hobby = hobby"
                    @click.stop="dialogDeletehobby = true"
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
export default {
  name: "Dashboard",
  computed: {
    ...mapState(["APIData"]),
    years() {
      let today = new Date();
      let year = today.getFullYear();
      return Array.from(
        { length: year - 1900 },
        (value, index) => 1901 + index
      );
    },
  },
  components: { Navbar },
  data() {
    return {
      info: {},
      infos: [],
      skill: {},
      skills: [],
      work: {},
      works: [],
      talent: {},
      talents: [],
      hobby: {},
      hobbies: {},
      education: {},
      educations: [],
      picture: {},
      pictures: [],
      experience: {},
      experiences: [],
      accountid: {},
      pictureid: {},
      formTitleEditSkill: "ทักษะ (แก้ไข)",
      formTitleEditEducation: "การศึกษา (แก้ไข)",
      formTitleEditExperience: "การทำงาน (แก้ไข)",
      formTitleEditInfo: "ข้อมูลส่วนตัว (แก้ไข)",
      formTitleEditTalent: "ความสามารถพิเศษ (แก้ไข)",
      formTitleEditHobby: "งานอดิเรก (แก้ไข)",
      formTitleEditWork: "ผลงาน (แก้ไข)",
      dialogDeletepicture: false,
      dialogediteducation: false,
      dialogDeleteEducation: false,
      dialogeditexperience: false,
      dialogDeleteexperience: false,
      dialogedittalent: false,
      dialogDeletetalent: false,
      dialogeditskill: false,
      dialogDeleteskill: false,
      dialogeditinfo: false,
      dialogDeleteinfo: false,
      dialogedithobby: false,
      dialogDeletehobby: false,
      dialogeditwork: false,
      dialogDeletework: false,
      messageeditinfo: "",
      messageeditskill: "",
      messageedittalent: "",
      messageeditexperience: "",
      messageediteducation: "",
      messageedithobby: "",
      messageeditwork: "",
      headerseducation: [
        { text: "ระดับ", align: "start", sortable: false },
        { text: "สถานศึกษา", sortable: false },
        { text: "ปีที่เข้าศึกษา", sortable: false },
        { text: "ปีที่จบการศึกษา", sortable: false },
      ],
      headersinfo: [
        { text: "ชื่อ", sortable: false },
        { text: "นามสกุล", sortable: false },
        { text: "อีเมล", sortable: false },
        { text: "หมายเลขโทรศัพท์", sortable: false },
        { text: "ที่อยู่", sortable: false },
      ],
      headerstalent: [
        { text: "ความสามารถด้าน", align: "start", sortable: false },
        { text: "รายอะเอียด", sortable: false },
      ],
      headersskill: [
        { text: "ทักษะด้าน", align: "start", sortable: false },
        { text: "รายละเอียด", sortable: false },
      ],
      headersexperience: [
        { text: "งาน", align: "start", sortable: false },
        { text: "ปีที่เริ่มเข้าทำงาน", align: "start", sortable: false },
        { text: "ปีที่จบจากงาน", align: "start", sortable: false },
        { text: "รายละเอียด", sortable: false },
      ],
      headershobby: [{ text: "งานอดิเรก", align: "start", sortable: false }],
      headerswork: [
        { text: "ผลงาน", align: "start", sortable: false },
        { text: "รายอะเอียด", align: "start", sortable: false },
      ],
      educationdegree: [
        "มัธยมศึกษา",
        "ประกาศนียบัตรวิชาชีพ (ปวช.)",
        "ประกาศนียบัตรวิชาชีพชั้นสูง (ปวส.)",
        "ปริญญาตรี",
        "ปริญญาโท",
        "ปริญญาเอก",
      ],
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
      document.getElementById("message").style.color = "red";
      this.messageeditinfo = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
      this.messageediteducation = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
      this.messageeditexperience = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
      this.messageedithobby = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
      this.messageeditskill = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
      this.messageeditwork = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
      this.messageedittalent = "แก้ไขไม่สำเร็จ เกิดข้อผิดพลาด";
    },
    setFormData() {
      this.experience = {};
      this.info = {};
      this.education = {};
      this.picture = {};
      this.hobby = {};
      this.work = {};
      this.messageeditinfo = "";
      this.messageeditskill = "";
      this.messageedittalent = "";
      this.messageeditexperience = "";
      this.messageediteducation = "";
      this.messageedithobby = "";
      this.messageeditwork = "";
    },
    closeDelete() {
      this.getAPIData();
      this.dialogDeleteskill = false;
      this.dialogDeleteEducation = false;
      this.dialogDeleteexperience = false;
      this.dialogDeleteinfo = false;
      this.dialogDeletetalent = false;
      this.dialogDeletepicture = false;
      this.dialogDeletehobby = false;
      this.dialogDeletework = false;
    },
    closeEdit() {
      this.getAPIData();
      this.dialogeditskill = false;
      this.dialogediteducation = false;
      this.dialogeditexperience = false;
      this.dialogedittalent = false;
      this.dialogeditinfo = false;
      this.dialogedithobby = false;
      this.dialogeditwork = false;
      this.setFormData();
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
            detail: this.skill.detail,
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
          this.getFailedEditMessage();
        });
    },
    async deleteItemConfirmHobby(hobby) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/hobbies/${hobby.hobbyid}/`, {
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
    async editItemConfirmHobby(hobby) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/hobbies/${hobby.hobbyid}/`,
          {
            accountid: this.accountid,
            hobbyid: this.hobby.hobbyid,
            name: this.hobby.name,
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
    async deleteItemConfirmExperience(experience) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/experiences/${experience.experienceid}/`, {
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
    async editItemConfirmExperience(experience) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/experiences/${experience.experienceid}/`,
          {
            accountid: this.accountid,
            experienceid: this.experience.experienceid,
            name: this.experience.name,
            datestart: this.experience.datestart,
            dateend: this.experience.dateend,
            detail: this.experience.detail,
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
    async deleteItemConfirmTalent(talent) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/talents/${talent.talentid}/`, {
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
    async editItemConfirmTalent(talent) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/talents/${talent.talentid}/`,
          {
            accountid: this.accountid,
            talentid: this.talent.talentid,
            name: this.talent.name,
            detail: this.talent.detail,
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
    async deleteItemConfirmInfo(info) {
      await this.getAccountid();
      await axiosBase
        .delete(`api/infos/${info.infoid}/`, {
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
    async editItemConfirmInfo(info) {
      await this.getAccountid();
      await axiosBase
        .put(
          `api/infos/${info.infoid}/`,
          {
            accountid: this.accountid,
            name: this.info.name,
            surname: this.info.surname,
            email: this.info.email,
            telphoneNumber: this.info.telphoneNumber,
            address: this.info.address,
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
    async deleteItemConfirmPicture() {
      await this.getPictureid();
      await axiosBase
        .delete(`api/pictures/${this.pictureid[0].pictureid}/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then(() => {
          this.closeDelete();
          this.setFormData();
          this.getSuccessDeleteMessage();
          this.fetchStatusMessage();
          this.getAPIData();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    fetchStatusMessage() {
      setInterval(this.setStatusMessage, 5000);
    },
    gotoAddEducationPage() {
      this.$router.push({ name: "Education" });
    },
    gotoAddSkillPage() {
      this.$router.push({ name: "Skill" });
    },
    gotoAddTalentPage() {
      this.$router.push({ name: "Talent" });
    },
    gotoAddExperiencePage() {
      this.$router.push({ name: "Experience" });
    },
    gotoAddInfoPage() {
      this.$router.push({ name: "Info" });
    },
    gotoAddPicturePage() {
      this.$router.push({ name: "Picture" });
    },
    gotoAddHobbyPage() {
      this.$router.push({ name: "Hobby" });
    },
    gotoAddWorkPage() {
      this.$router.push({ name: "Work" });
    },
  },
};
</script>
