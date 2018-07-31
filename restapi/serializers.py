from rest_framework import serializers
from restapi.models import Portfolios
from django.contrib.auth.models import User


class PortfolioSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Portfolios
        fields = ('id', 'title', 'pro_loss', 'created', 'owner')


class UserSerializer(serializers.ModelSerializer):
    portfolio = serializers.PrimaryKeyRelatedField(many=True, queryset=Portfolios.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'portfolio')