from rest_framework import serializers

class CustomPointSerializer(serializers.Serializer):
    title = serializers.CharField()
    matter = serializers.CharField()
    class Meta:
        fields = ["title","matter"]
        extra_kwargs = {'title':{'required':True,"max_length":500},
                        'matter':{'required':True,"max_length":500}}