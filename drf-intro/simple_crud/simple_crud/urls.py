from rest_framework import routers
from measurements.views import ProjectsViewSet, MeasurementsViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectsViewSet)
router.register('measurements', MeasurementsViewSet)

urlpatterns = router.urls
