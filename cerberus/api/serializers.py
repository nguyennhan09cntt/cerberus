from rest_framework import serializers

# Serializers define the API representation.
class ClassifySerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()