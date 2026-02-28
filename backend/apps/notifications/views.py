from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer, NotificationCreateSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return NotificationCreateSerializer
        return NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
