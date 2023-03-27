from django.urls import path
from Pokemon import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("pokemon/adds",views.registerPokemon, name="register-csv-pokemon"),
    path("pokemon",views.pokemon, name="all-detail-filter"),
    path("pokemon/",views.pokemon, name="all-detail-filter"),
    path("pokemon/<str:id>",views.pokemon, name="all-detail-filter"),
    path("type/add",views.registerPokemonType, name="all-type"),
    path("type",views.type, name="all-type"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)