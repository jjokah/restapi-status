from django.contrib.auth import get_user_model

from rest_framework import serializers

from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()


# serializer for a user detail
class UserDetailSerializer(serializers.ModelSerializer):
    uri                 = serializers.SerializerMethodField(read_only=True)
    status              = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status' # model name
        ]

    def get_uri(self, obj):
        return "/api/user/{id}/".format(id=obj.id)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 2
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.status_set.all().order_by("-timestamp") # Status.object.filter(user=obj)
        data = {
            'uri': self.get_uri(obj) + "status/",
            'last': StatusInlineUserSerializer(qs.first()).data,
            'recent': StatusInlineUserSerializer(qs[:limit], many=True).data
        }
        return data


