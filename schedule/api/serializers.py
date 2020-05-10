from rest_framework import serializers

from schedule.models import (Teacher)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
