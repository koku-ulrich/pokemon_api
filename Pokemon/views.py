import pandas as pd
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db.models import Q
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView
from pathlib import Path
from Pokemon.models import Pokemon,Type
from Pokemon.serializers import PokemonSerializer,TypeSerializer,PokemonDetailSerializer
from django.core.files.storage import default_storage


# Create our views here.
@csrf_exempt
# create all pokemon request
def pokemon(request, id="000"): # required variable will work only on  GET
    # request for method POST
    if request.method=='POST':
        # get request data
        data=JSONParser().parse(request)
        # check if request data has limit if not set it to 20
        if 'show' not in data:
            data['show'] = 5
        if 'page' not in data:
            data['page'] = 1

        # set OFFSET for pagination result
        OFFSET = ( int(data['show']) * int(data['page']) ) - int(data['show'])
        LIMIT = int(data['show']) * int(data['page'])

        pokemon = Pokemon.objects.all()

        # check if request data has field name
        if 'name' in data:

            # check if request data has also type field
            if 'type' in data :
                # get pokemon list with filter
                pokemon = Pokemon.objects.filter(
                    #filter if pokemon name contain request name
                    Q(name__contains=data['name'].lower()) &
                    # additional filter
                    Q(
                        #filter if pokemon type1 contain request type
                        Q(type1__contains = data['type'].lower()) |
                        #filter if pokemon type1 contain request type
                        Q(type2__contains  = data['type'].lower())
                    )
                )

            #  if request data has only name field
            else :
                # get pokemon filter by name
                pokemon = Pokemon.objects.filter(name__contains=data['name'].lower())

        #  if request data has only type field
        elif 'type' in data :
            # get pokemon filter type1 and type2
            pokemon = Pokemon.objects.filter(
                Q(type1__contains = data['type'].lower()) |
                Q(type2__contains  = data['type'].lower())
            )

        # calculate all page by how row to show
        pages = int(pokemon.count() / int(data['show']) )+ 1

        # serial query and set OFFSET and LIMIT
        serializer=PokemonSerializer(pokemon[OFFSET:LIMIT],many=True)
        return JsonResponse({'pokemon' : serializer.data, 'pages': pages },safe=False)

    elif request.method=='GET' :
        if int(id) > 0 :
            pokemon = Pokemon.objects.get(id=id)
            serializer=PokemonDetailSerializer(pokemon,many=False)
            return JsonResponse({'pokemon' : serializer.data},safe=False)

# Create your views here.
@csrf_exempt
def type(request, id=0):
    if request.method=='GET' :
        if int(id) > 0 :
            type = Type.objects.get(id=id)
            serializer=TypeSerializer(type,many=False)
            return JsonResponse({'types' : serializer.data},safe=False)
        else :
            types = Type.objects.all()
            serializer=TypeSerializer(types,many=True)
            return JsonResponse({'types' : serializer.data},safe=False)

def registerPokemon(request):
    """Upload data from CSV, with validation."""
    if request.method=='GET':
        # import csv data
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
                    print(row[column])
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
        return JsonResponse(message,safe=False)

def registerPokemonType(request):
    """Upload data from CSV, and select ditinct type"""
    if request.method=='GET':
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
        return JsonResponse(message,safe=False)