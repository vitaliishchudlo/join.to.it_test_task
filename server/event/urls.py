from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, EventSubscriptionViewSet, EventSubscribeView

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'subscriptions', EventSubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('events/<int:event_id>/subscribe/', EventSubscribeView.as_view(), name='event-subscribe'),
]
