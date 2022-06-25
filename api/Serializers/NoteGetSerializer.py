from rest_framework import serializers

class NoteGetSerializer(serializers.Serializer):
    title = serializers.CharField()

    class Meta:
        fields = ('title')
        extra_kwargs = {
            "title":{'required':True}
        }