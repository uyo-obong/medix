from rest_framework import serializers

from medixus.apps.new_feature.models import GestationalTable


class GestationalSerializer(serializers.ModelSerializer):

    class Meta:
        model = GestationalTable
        fields = ("age", "medical_history", "documents", "gender",
                  "volunteer_health", "height", "unit_of_height", "weight", "unit_of_weight",
                  "temperature", "unit_of_temperature" "ture", "blood_pressure",
                  "unit_of_blood_pressure")




