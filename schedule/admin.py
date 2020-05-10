from django.contrib import admin

from schedule.models import (Teacher, Group, Lesson, Exercise)

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Exercise)
