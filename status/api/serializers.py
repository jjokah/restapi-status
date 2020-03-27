from rest_framework import serializers

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


# status serializer for a users
class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image',
        ]

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    uri         = serializers.SerializerMethodField(read_only=True)
    user        = UserPublicSerializer(read_only=True) # nested serializer
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image',
        ]

        read_only_fields = ['user'] # GET

    def get_uri(self, obj):
        return "/api/status/{id}/".format(id=obj.id)

    # validate serializer - to require Content or Image
    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data