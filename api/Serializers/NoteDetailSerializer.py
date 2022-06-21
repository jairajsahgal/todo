from api.Model.Account import Note
from rest_framework import serializers

class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title"]