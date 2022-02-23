from rest_framework import serializers
from .models import Users,Organization,Campaigns
class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ['Email_Address','password']

    def create(self, validated_data):
        user = Users.objects.create(Email_Address = validated_data['Email_Address'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    



class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = "__all__"


class OrganizationSerializer(serializers.Serializer):
    campaigns_name = serializers.CharField()
    Organization_address = serializers.CharField()
    Organization_city  = serializers.CharField()
    Organization_user = serializers.EmailField()

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)
