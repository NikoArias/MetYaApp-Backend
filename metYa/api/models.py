from django.db import models



class Event(models.Model):
    event_name = models.TextField()
    event_address = models.TextField()
    event_pc = models.TextField()
    event_dt = models.DateTimeField()
    event_details = models.TextField()
