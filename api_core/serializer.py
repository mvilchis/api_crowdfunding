from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField,CurrentUserDefault

from models import ProjectDonation, UserDonation, FundingDonation
from models import ProjectRecompesas, UserRecompensas, FundingRecompensas
from models import ProjectCapital, UserCapital, FundingCapital
from models import ProjectDeuda, UserDeuda, FundingDeuda
from rest_framework.fields import CurrentUserDefault

class ProjectDonationSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = ProjectDonation
        exclude = ('id', )


class UserDonationSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserDonation
        exclude = ('id', )

class FundingDonationSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDonation
        exclude = ('id', )


class ProjectRecompesasSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectRecompesas
        exclude = ('id', )


class UserRecompensasSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserDonation
        exclude = ('id', )


class FundingRecompensasSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDonation
        exclude = ('id', )


class ProjectCapitalSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectCapital
        exclude = ('id', )

class UserCapitalSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserCapital
        exclude = ('id', )

class FundingCapitalSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingCapital
        exclude = ('id', )


class ProjectDeudaSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectDeuda
        exclude = ('id', )


class UserDeudaSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = UserDeuda
        exclude = ('id', )

class FundingDeudaSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDeuda
        exclude = ('id', )
