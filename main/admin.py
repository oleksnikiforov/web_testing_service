from django.contrib import admin

from main.models import Student, Teacher, Group, Problem, Lecture


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Problem)
admin.site.register(Lecture)
