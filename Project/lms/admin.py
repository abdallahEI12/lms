from django.contrib import admin
from lms.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Exam)