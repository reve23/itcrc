from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField
from .models import Event,Segment

class SegmentSerializer(ModelSerializer):
    icon_url = SerializerMethodField('get_icon_url')
    class Meta:
        model= Segment
        fields= ['id', 'icon_url','name', 'rules','reg_last_date']
    def get_icon_url(self,obj):
        return obj.icon.url

class EventSerializer(ModelSerializer):
    segment = SegmentSerializer(many=True)
    image_url = SerializerMethodField('get_image_url')
    class Meta:
        model = Event
        fields= ['id','image_url','name','segment','short_description','rules','date']
    
    def get_image_url(self,obj):
        return obj.thumbnail.url