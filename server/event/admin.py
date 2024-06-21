from django.contrib import admin

from .models import Event, EventSubscription

admin.site.register(Event)
admin.site.register(EventSubscription)
