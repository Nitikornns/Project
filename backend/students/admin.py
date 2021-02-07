from django.contrib import admin
from .models import Student, Skill, Language, Picture, Work, Education

# Register your models here.
admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Picture)
admin.site.register(Work)
admin.site.register(Education)
