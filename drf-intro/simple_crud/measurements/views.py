from rest_framework.viewsets import ModelViewSet

from .models import Project, Measurement
from .serializers import MeasurementSerializer, ProjectSerializer


class ProjectsViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class MeasurementsViewSet(ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
