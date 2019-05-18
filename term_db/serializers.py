from .models import Terminal, MeasuredData
from rest_framework import serializers


class TerminalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Terminal
        fields = ('name', 'latitude', 'longitude', 'url')


class MeasuredDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MeasuredData
        fields = ('temperature', 'pressure', 'humidity', 'added_at', 'terminal')
