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
        #select all to default pokemon
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
    # if request with get methode
    elif request.method=='GET' :
        #if id > 0
        if int(id) > 0 :
            # get Pokemon by ID
            pokemon = Pokemon.objects.get(id=id)
            serializer=PokemonDetailSerializer(pokemon,many=False)
            return JsonResponse({'pokemon' : serializer.data},safe=False)

# Create your views here.
@csrf_exempt
def type(request, id=0):
    #check if request methode is GET
    if request.method=='GET' :
        # check if id is int and >0
        if int(id) > 0 :
            #get type by Id
            type = Type.objects.get(id=id)
            serializer=TypeSerializer(type,many=False)
            return JsonResponse({'types' : serializer.data},safe=False)
        else :
            #get type by Id
            types = Type.objects.all()
            serializer=TypeSerializer(types,many=True)
            return JsonResponse({'types' : serializer.data},safe=False)