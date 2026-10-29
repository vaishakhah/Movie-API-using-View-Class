#using model serializer
from rest_framework import serializers
from MovieAPP.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields = "__all__"

    def validate(self, data):
        if data['rating'] < 0:
            raise serializers.ValidationError("rating should not be less than zero")
        return data


