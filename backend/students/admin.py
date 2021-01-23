from django.contrib import admin
from .models import Student, Skill, Language


# Register your models here.
admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(Language)
