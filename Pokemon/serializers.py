from rest_framework import serializers
from Pokemon.models import Pokemon,Type

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pokemon
        fields=('id','image_url','name','type1','type2')

class PokemonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pokemon
        fields=('id','image_url','name','type1','type2','total','hp','attack','sp_atk','defense','sp_def','speed','generation','legendary')

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type
        fields=('id','name')

