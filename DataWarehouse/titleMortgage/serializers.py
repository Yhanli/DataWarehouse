from rest_framework import serializers
from titleMortgage.models import *


class TitleMortgageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleMortgage
        fields = '__all__'
