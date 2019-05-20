from campaign.models import Campaign

from rest_framework import serializers


class CampaignSeriallizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'country', 'budget', 'goal', 'category')
