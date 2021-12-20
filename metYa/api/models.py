from django.db import models



class Event(models.Model):
    event_img = models.TextField()
    event_host = models.TextField()
    event_name = models.TextField()
    event_address = models.TextField()
    event_pc = models.TextField()
    event_dt = models.DateTimeField()
    event_details = models.TextField()
    event_lat = models.FloatField()
    event_long = models.FloatField()

class Profile(models.Model):
    user_f_name = models.TextField()
    user_l_name = models.TextField()
    user_descrip = models.TextField()
    F_link = models.TextField()
    T_link = models.TextField()
    I_link = models.TextField()
    S_link = models.TextField()
