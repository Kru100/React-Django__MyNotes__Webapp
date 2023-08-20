from rest_framework.serializers import ModelSerializer
from .models import Note

class Noteserializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','body', 'updated']
        