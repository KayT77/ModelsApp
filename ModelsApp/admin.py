from django.contrib import admin
from .models import School, Faculty, Department, Grade, Certificate_type, Student
# Register your models here.

admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Certificate_type)
admin.site.register(Student)