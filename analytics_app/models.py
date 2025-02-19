from django.db import models
from django.utils import timezone

class VisitorRecord(models.Model):
    store_id = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    unique_visitors = models.IntegerField()

    def __str__(self):
        return f"{self.date} - Store: {self.store_id} - Visitors: {self.unique_visitors}"

    class Meta:
        ordering = ['-date']  # Order by date descending
