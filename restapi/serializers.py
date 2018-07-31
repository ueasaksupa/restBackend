from rest_framework import serializers
from restapi.models import Portfolios


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolios
        fields = ('id', 'title', 'pro_loss', 'created')