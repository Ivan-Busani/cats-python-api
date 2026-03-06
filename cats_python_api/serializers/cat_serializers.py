from rest_framework import serializers
from cats_python_api.models.core_models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'cat_id', 'url', 'width', 'height', 'breeds', 'api_used', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']  # api_used set by view
