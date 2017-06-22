from rest_framework.serializers import ModelSerializer

from models import ProyectDonation, UserDonation, FundingDonation

class ProyectDonationSerializer(ModelSerializer):
    class Meta:
        model = ProyectDonation
        fields = '__all__'

class UserDonationSerializer(ModelSerializer):
    class Meta:
        model = UserDonation
        fields = '__all__'

class FundingDonationSerializer(ModelSerializer):
    class Meta:
        model = FundingDonation
        fields = '__all__'
