from rest_framework import serializers
from .models import AssetTransportRequest, ShareTravelInfo

class AssetTransportRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetTransportRequest
        fields = '__all__'
        
    def validate(self, data):
        # validate asset type
        asset_types = ['LAPTOP', 'TRAVEL_BAG', 'PACKAGE']
        if data['asset_type'] not in asset_types:
            raise serializers.ValidationError("Invalid asset type")
        # validate sensitivity
        sensitivities = ['HIGHLY_SENSITIVE', 'SENSITIVE', 'NORMAL']
        if data['asset_sensitivity'] not in sensitivities:
            raise serializers.ValidationError("Invalid sensitivity")
        return data


class ShareTravelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareTravelInfo
        fields = '__all__'


class MatchedRidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareTravelInfo
        fields = ['id','from_location', 'to_location', 'date_time', 'travel_medium', 'status']