from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField
from .models import Event,Segment,Rules,SegmentRule


class SegmentRuleSerializer(ModelSerializer):
    class Meta:
        model = SegmentRule
        fields = ('__all__')
class SegmentSerializer(ModelSerializer):
    icon_url = SerializerMethodField('get_icon_url')
    segment_rules = SegmentRuleSerializer(many=True)
    class Meta:
        model= Segment
        fields= ['id', 'icon_url','name', 'segment_rules','reg_last_date']
    def get_icon_url(self,obj):
        return obj.icon.url

class RulesSerializer(ModelSerializer):
    class Meta:
        model = Rules
        fields = ('__all__')
class EventSerializer(ModelSerializer):
    segment = SegmentSerializer(many=True)
    event_rules = RulesSerializer(many=True)
    image_url = SerializerMethodField('get_image_url')
    class Meta:
        model = Event
        fields= ['id','image_url','name','event_rules','segment','short_description','date']
        depth = 2
    
    def get_image_url(self,obj):
        return obj.thumbnail.url
    