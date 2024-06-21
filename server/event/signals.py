from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Event, EventSubscription


@receiver(post_save, sender=EventSubscription)
def send_subscription_email(sender, instance, created, **kwargs):
    if created:
        event = instance.event
        subject = 'Subscription Confirmation'
        message = f'Dear {instance.user.username},\n\n' \
                  f'You have successfully subscribed to the event "{event.title}".\n' \
                  f'Event details:\n' \
                  f'Date: {event.date}\n' \
                  f'Location: {event.location}\n\n' \
                  f'Thank you for subscribing.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.user.email],
            fail_silently=False,
        )


@receiver(pre_delete, sender=Event)
def send_event_cancellation_email(sender, instance, **kwargs):
    subscriptions = EventSubscription.objects.filter(event=instance)
    for subscription in subscriptions:
        subject = 'Event Cancellation'
        message = f'Dear {subscription.user.username},\n\n' \
                  f'The event "{instance.title}" scheduled for {instance.date} at {instance.location} has been cancelled.\n' \
                  f'We apologize for the inconvenience.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [subscription.user.email],
            fail_silently=False,
        )
