from api.Model.Account import Note
from rest_framework import serializers
import logging
logger = logging.getLogger('django')


class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title"]