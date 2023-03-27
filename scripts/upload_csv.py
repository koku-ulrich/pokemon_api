import sys
import pandas as pd
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models import Q
from pathlib import Path
from Pokemon.models import Pokemon,Type
from Pokemon.serializers import PokemonSerializer,TypeSerializer,PokemonDetailSerializer
from django.core.files.storage import default_storage

def run():
#"""Upload data from CSV, with validation."""
    data = pd.read_csv(Path(__file__).resolve().parent.parent /"Pokemon/pokemon.csv")
    # init message as json
    message = {}
    # for row in data
    for index,row in data.iterrows():
        # for column name in columns add item in pokemon
        pokemon = {}
        for column in data.columns :
            #create json pokem json to post pokemon serializer
            if column.lower() == 'id':
                pokemon[column.lower()] = format(row[column], '03d')
                pokemon['image_url'] = 'https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/'+pokemon[column.lower()]+'.png'
            #elif column in ['image_url','type1','type2']:
            elif isinstance(row[column], str):
                pokemon[column.lower()] = row[column].lower()
            else :
                pokemon[column.lower()] = row[column]
        # save pokemon to sqlite
        serializer=PokemonSerializer(data=pokemon)
        # init message index as json
        message[index] = {}
        if serializer.is_valid():
            serializer.save()
            message[index]['success'] = "add Successfully"
        else :
            message[index]['errors'] = serializer.errors
    print(message)

def run():
#"""Upload type from CSV"""
# import csv data
    data = pd.read_csv(Path(__file__).resolve().parent.parent /"Pokemon/pokemon.csv")
    types = pd.concat([data['Type1'], data['Type2']]).unique()
    types = types[~pd.isnull(types)]
    print(types)
    # init message as json
    message = {}
    for index in types:
        type = {"name" : index}
        # save type to sqlite
        serializer=TypeSerializer(data=type)
        # init message as json
        message[index] = {}
        if serializer.is_valid():
            serializer.save()
            message[index]['success'] = "add Successfully"
        else :
            message[index]['errors'] = serializer.errors
    print(message)