# Generated by Django 4.1.7 on 2023-03-25 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Pokemon", "0002_alter_pokemons_attack_alter_pokemons_defense_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Departments",),
        migrations.DeleteModel(name="Employees",),
    ]
