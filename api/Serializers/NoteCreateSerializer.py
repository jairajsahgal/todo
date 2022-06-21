from api.Model.Account import Note
from rest_framework import serializers

class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title']