from rest_framework import serializers

from .models import Project, Measurement


class ProjectPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.name


class MeasurementSerializer(serializers.ModelSerializer):
    value = serializers.FloatField(required=True)
    project = ProjectPrimaryKeyRelatedField(queryset=Project.objects.all())
    image = serializers.ImageField(allow_null=True, allow_empty_file=False)

    class Meta:
        model = Measurement
        fields = 'value', 'created_at', 'updated_at', 'image', 'project'


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    longitude = serializers.FloatField
    latitude = serializers.FloatField

    class Meta:
        model = Project
        fields = 'name', 'longitude', 'latitude', 'created_at', 'updated_at'
