from re import U
from rest_framework import serializers
from .models import Users,Organization,Campaigns
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "name",
            "Email_Address",
            "password",
            "organization_admin",
            "oganiztioncontroller"
        ]

    
    # Email_Address = serializers.EmailField()
    # password = serializers.CharField()
    # name = serializers.CharField()
    # organization_admin = serializers.BooleanField(default=False)
    # oganiztioncontroller = serializers.BooleanField(default=False)
 

    def create(self, validated_data):
        user = Users.objects.create(Email_Address = validated_data['Email_Address'])
        user.set_password(validated_data['password'])
        user.organization_admin = validated_data["organization_admin"]
        user.oganiztioncontroller = validated_data["oganiztioncontroller"]
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
