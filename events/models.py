from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
    
class Event(models.Model):
    thumbnail = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
class Rules(models.Model):
    event = models.ForeignKey(Event,related_name='event_rules',on_delete=models.SET_NULL,null=True,blank=True)
    rule = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.rule
    


class Segment(models.Model):
    event = models.ForeignKey(Event,related_name='segment',on_delete=models.SET_NULL,null=True,blank=True)
    icon = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    reg_last_date = models.DateTimeField()

    def __str__(self):
        return self.name
class SegmentRule(models.Model):
    segment = models.ForeignKey(Segment,related_name='segment_rules',on_delete=models.SET_NULL,null=True,blank=True)
    rule = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.rule
    