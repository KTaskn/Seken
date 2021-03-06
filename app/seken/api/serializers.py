
from rest_framework import serializers
from .models import Newspaper, Word

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ('name', 'url')


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'newspaper', '_datetime')

class WordRankingSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    class Meta:
        model = Word
        fields = ('word', 'count')