from rest_framework.serializers import ModelSerializer
from .models import Note
from django.db.models import fields
class NoteSerializer(ModelSerializer):
    class Meta:
        model=Note
        fields=['id','title','description','pub_date','importance']