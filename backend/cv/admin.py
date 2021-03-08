from django.contrib import admin
from .models import Info, Skill, Language, Picture, Work, Education

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'degree']


class InfoAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name',
                    'surname', 'email', 'telphoneNumber']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'degree']


class PictureAdmin(admin.ModelAdmin):
    list_display = ['accountid']


class WorkAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'name', 'detail']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['accountid', 'degree', 'name', 'datestart', 'dateend']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
