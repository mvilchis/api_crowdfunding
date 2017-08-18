################    REST Libraries      ##################
from rest_framework import serializers
from rest_framework.serializers import (PrimaryKeyRelatedField,
                                        CurrentUserDefault)

from rest_framework_bulk import (BulkListSerializer,
                                 BulkSerializerMixin,)

################          My code       ##################
from models import (ProjectDonation,
                    ProjectRecompesas,
                    ProjectCapital,
                    ProjectDeuda,
                    UserDonation,
                    UserRecompensas,
                    UserCapital,
                    UserDeuda,
                    FundingDonation,
                    FundingRecompensas,
                    FundingCapital,
                    FundingDeuda)

class ProjectDonationSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = ProjectDonation
        exclude = ('id','user' )
        list_serializer_class = BulkListSerializer



class UserDonationSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserDonation
        exclude = ('id', 'user' )
        list_serializer_class = BulkListSerializer


class FundingDonationSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDonation
        exclude = ('id', 'user' )
        list_serializer_class = BulkListSerializer



class ProjectRecompesasSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectRecompesas
        exclude = ('id', 'user' )
        list_serializer_class = BulkListSerializer



class UserRecompensasSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserDonation
        exclude = ('id', 'user')
        list_serializer_class = BulkListSerializer


class FundingRecompensasSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDonation
        exclude = ('id', 'user')
        list_serializer_class = BulkListSerializer



class ProjectCapitalSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectCapital
        exclude = ('id', 'user' )

class UserCapitalSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = UserCapital
        exclude = ('id', 'user')
        list_serializer_class = BulkListSerializer

class FundingCapitalSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingCapital
        exclude = ('id', 'user')
        list_serializer_class = BulkListSerializer


class ProjectDeudaSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = ProjectDeuda
        exclude = ('id','user' )
        list_serializer_class = BulkListSerializer


class UserDeudaSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = UserDeuda
        exclude = ('id', 'user')
        list_serializer_class = BulkListSerializer

class FundingDeudaSerializer(BulkSerializerMixin,serializers.ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = FundingDeuda
        exclude = ('id', 'user')
        list_serializer_class = BulkListSerializer
