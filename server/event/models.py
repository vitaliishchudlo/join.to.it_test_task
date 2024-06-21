from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} | {self.location}"


class EventSubscription(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event',)

    def __str__(self) -> str:
        return f"{self.user} subscribed to {self.event}"
