from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from advertisements.permissions import OnlyOwnerCanEdit
from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement
from advertisements.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend



@permission_classes([OnlyOwnerCanEdit, IsAuthenticated])
class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    filterset_fields = ['creator_id', 'status', 'created_at']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [OnlyOwnerCanEdit(),IsAuthenticated()]
        return []
