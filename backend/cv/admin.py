from django.contrib import admin
from .models import Info, Skill, Talent, Language, Picture, Experience, Education, Hobby, Work

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'detail']


class TalentAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'detail']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'detail']


class HobbyAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name']


class InfoAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name',
                    'surname', 'email', 'telphoneNumber', 'address']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'degree']


class PictureAdmin(admin.ModelAdmin):
    list_display = ['accountid']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'detail', 'datestart', 'dateend']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'degree', 'name', 'datestart', 'dateend']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Talent, TalentAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Work, WorkAdmin)
