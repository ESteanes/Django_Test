from rest_framework import serializers
from countriesapp.models import Countries


class CountriesAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = ('id', 'name', 'capital')
