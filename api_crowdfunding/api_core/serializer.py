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
        exclude = ('id','user' )


class UserDonationSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserDonation
        exclude = ('id', 'user' )

class FundingDonationSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDonation
        exclude = ('id', 'user' )


class ProjectRecompesasSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectRecompesas
        exclude = ('id', 'user' )


class UserRecompensasSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserDonation
        exclude = ('id', 'user')


class FundingRecompensasSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDonation
        exclude = ('id', 'user')


class ProjectCapitalSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectCapital
        exclude = ('id', 'user' )

class UserCapitalSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserCapital
        exclude = ('id', 'user')

class FundingCapitalSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingCapital
        exclude = ('id', 'user')


class ProjectDeudaSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectDeuda
        exclude = ('id','user' )


class UserDeudaSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = UserDeuda
        exclude = ('id', 'user')

class FundingDeudaSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDeuda
        exclude = ('id', 'user')
