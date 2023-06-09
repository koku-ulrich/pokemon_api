# Generated by Django 4.1.7 on 2023-03-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departments",
            fields=[
                ("DepartmentId", models.AutoField(primary_key=True, serialize=False)),
                ("DepartmentName", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                ("EmployeeId", models.AutoField(primary_key=True, serialize=False)),
                ("EmployeeName", models.CharField(max_length=500)),
                ("Department", models.CharField(max_length=500)),
                ("DateOfJoining", models.DateField()),
                ("PhotoFileName", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Pokemons",
            fields=[
                (
                    "Id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("Name", models.CharField(max_length=500, unique=True)),
                ("Type1", models.CharField(blank=True, max_length=500, null=True)),
                ("Type2", models.CharField(blank=True, max_length=500, null=True)),
                ("Hp", models.IntegerField(default=0)),
                ("Total", models.IntegerField(default=0)),
                ("Attack", models.IntegerField(default=0)),
                ("Defense", models.IntegerField(default=0)),
                ("SpAtk", models.IntegerField(default=0)),
                ("SpDef", models.IntegerField(default=0)),
                ("Speed", models.IntegerField(default=0)),
                ("Generation", models.IntegerField(default=0)),
                ("Legendary", models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
