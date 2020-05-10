from rest_framework import routers

from schedule.api.viewsets import (TeacherViewset)

router = routers.DefaultRouter()
router.register('Teacher', TeacherViewset)
