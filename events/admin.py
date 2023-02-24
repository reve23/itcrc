from django.contrib import admin
from django import forms
from .models import Event,Segment,Rules,SegmentRule
# Register your models here.

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['rules'].queryset = Rules.objects.exclude(event__pk=self.instance.pk)

    class Meta:
        model = Event
        fields = '__all__'

class EventAdmin(admin.ModelAdmin):
    form = EventForm
admin.site.register(Event,EventAdmin)
admin.site.register(Rules)
admin.site.register(SegmentRule)
admin.site.register(Segment)