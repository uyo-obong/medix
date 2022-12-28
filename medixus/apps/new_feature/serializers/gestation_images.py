from rest_framework import serializers

from medixus.apps.new_feature.models import GestationalImages


class GestationalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestationalImages
        fields = ("image", "gestation")
