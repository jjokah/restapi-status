from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializers import UserPublicSerializer
from status.models import Status


# main serializer for status
class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)  # nested serializer

    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image',
        ]

        read_only_fields = ['user']  # GET

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-status:detail',
                           kwargs={"id": obj.id},
                           request=request)

    # validate serializer - to require Content or Image
    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data


# status serializer for a user
class StatusInlineUserSerializer(StatusSerializer):
    class Meta:
        model = Status
        fields = [
            'uri',
            'id',
            'content',
            'image',
        ]
