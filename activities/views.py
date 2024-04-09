from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Activity
from .serializers import ActivitySerializer
from .tasks import send_event_to_azure

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        activity = serializer.save()
        summary = f"New activity created in project: {activity.project_name}"
        send_event_to_azure(summary)

    def perform_update(self, serializer):
        activity = serializer.save()
        summary = f"Activity updated in project: {activity.project_name}"
        send_event_to_azure(summary)
