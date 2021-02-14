from django.contrib import admin
from .models import Student, Skill, Language, Picture, Work, Education

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['accountid', 'name', 'degree']


class StudentAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['accountid', 'name',
                    'surname', 'email', 'telphoneNumber']


class LanguageAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['accountid', 'name', 'degree']


class PictureAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['accountid']


class WorkAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['accountid', 'name', 'detail']


class EducationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['accountid', 'degree', 'name', 'datestart', 'dateend']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
