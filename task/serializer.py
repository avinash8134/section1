from rest_framework import serializers
from task.models import Restaurant


class RestauSerialeizer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"