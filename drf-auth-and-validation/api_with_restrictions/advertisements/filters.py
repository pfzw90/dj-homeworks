from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    creator = filters.NumberFilter(field_name='creator_id')
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    
    order = filters. OrderingFilter(
         fields=(
            ('created_at', 'date'),
            ('status', 'status'),
        )
    )

    class Meta:
        model = Advertisement
        fields = ['status', 'creator_id', 'status']

