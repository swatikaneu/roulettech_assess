from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'file', 'uploaded_at', 'file_url']

    def get_file_url(self, obj):
        if obj.file:
            return self.context['request'].build_absolute_uri(obj.file.url)
        return None
