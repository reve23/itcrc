from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Rules(models.Model):
    rule = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.rule
    
class Event(models.Model):
    thumbnail = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    # rules = models.ForeignKey(Rules,on_delete=models.CASCADE,null=True,blank=True)
    rules = models.ManyToManyField(Rules,null=True,blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    

class SegmentRule(models.Model):
    rule = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.rule

class Segment(models.Model):
    event = models.ForeignKey(Event,related_name='segment',on_delete=models.SET_NULL,null=True,blank=True)
    icon = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    rules = models.ForeignKey(SegmentRule,on_delete=models.CASCADE,null=True,blank=True)
    reg_last_date = models.DateTimeField()

    def __str__(self):
        return self.name
    