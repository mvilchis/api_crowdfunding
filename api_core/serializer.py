from rest_framework.serializers import ModelSerializer

from models import ProjectDonation, UserDonation, FundingDonation
from models import ProjectRecompesas, UserRecompensas, FundingRecompensas
from models import ProjectCapital, UserCapital, FundingCapital
from models import ProjectDeuda, UserDeuda, FundingDeuda


class ProjectDonationSerializer(ModelSerializer):
    class Meta:
        model = ProjectDonation
        exclude = ('id', )


class UserDonationSerializer(ModelSerializer):
    class Meta:
        model = UserDonation
        exclude = ('id', )


class FundingDonationSerializer(ModelSerializer):
    class Meta:
        model = FundingDonation
        exclude = ('id', )


class ProjectRecompesasSerializer(ModelSerializer):
    class Meta:
        model = ProjectRecompesas
        exclude = ('id', )


class UserRecompensasSerializer(ModelSerializer):
    class Meta:
        model = UserDonation
        exclude = ('id', )


class FundingRecompensasSerializer(ModelSerializer):
    class Meta:
        model = FundingDonation
        exclude = ('id', )


class ProjectCapitalSerializer(ModelSerializer):
    class Meta:
        model = ProjectCapital
        exclude = ('id', )


class UserCapitalSerializer(ModelSerializer):
    class Meta:
        model = UserCapital
        exclude = ('id', )


class FundingCapitalSerializer(ModelSerializer):
    class Meta:
        model = FundingCapital
        exclude = ('id', )


class ProjectDeudaSerializer(ModelSerializer):
    class Meta:
        model = ProjectDeuda
        exclude = ('id', )


class UserDeudaSerializer(ModelSerializer):
    class Meta:
        model = UserDeuda
        exclude = ('id', )


class FundingDeudaSerializer(ModelSerializer):
    class Meta:
        model = FundingDeuda
        exclude = ('id', )
