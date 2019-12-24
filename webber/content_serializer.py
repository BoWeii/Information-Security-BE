from .models import Content
from rest_framework.serializers import ModelSerializer


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        field = '__all__'
