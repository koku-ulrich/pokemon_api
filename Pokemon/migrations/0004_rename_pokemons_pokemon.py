# Generated by Django 4.1.7 on 2023-03-26 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Pokemon", "0003_delete_departments_delete_employees"),
    ]

    operations = [
        migrations.RenameModel(old_name="Pokemons", new_name="Pokemon",),
    ]
