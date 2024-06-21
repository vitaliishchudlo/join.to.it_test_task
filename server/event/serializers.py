from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Event, EventSubscription


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class EventSerializer(ModelSerializer):
    organizer = UserSerializer()

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'location', 'organizer')


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Date must be in the future")
        return value


class EventSubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    event = EventSerializer()

    class Meta:
        model = EventSubscription
        fields = ('id', 'user', 'event')
