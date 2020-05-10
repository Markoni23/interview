from rest_framework import viewsets

from schedule.models import (Teacher)
from .serializers import TeacherSerializer


class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
