from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Event, EventSubscription
from .serializers import EventSerializer, EventCreateSerializer, EventSubscriptionSerializer


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EventSerializer
        return EventCreateSerializer


class EventSubscriptionViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSubscriptionSerializer

    def get_queryset(self):
        return EventSubscription.objects.filter(user=self.request.user)  # show only subscriptions of the current user
        # return EventSubscription.objects.all() # show all subscriptions to all users


class EventSubscribeView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSubscriptionSerializer

    def create(self, request, *args, **kwargs):
        try:
            event = Event.objects.get(id=kwargs.get('event_id'))
            subscription, created = EventSubscription.objects.get_or_create(user=request.user, event=event)
            if created:
                serializer = self.get_serializer(subscription)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": "Already subscribed"}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({"detail": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
