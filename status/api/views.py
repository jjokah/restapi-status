from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissions import IsOwnerOrReadOnly
from status.models import Status
from .serializers import StatusSerializer


# Detail View class for each status
class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # authentication_classes  = []
    serializer_class        = StatusSerializer
    queryset                = Status.objects.all()
    lookup_field            = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# List view class for all status
class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes  = [SessionAuthentication]
    serializer_class        = StatusSerializer
    passed_id               = None
    search_fields           = ('user__username', 'content', 'user__email')
    ordering_fields         = ('user__username', 'timestamp')
    queryset                = Status.objects.all()


    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
