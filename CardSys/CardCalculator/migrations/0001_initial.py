# Generated by Django 3.1.2 on 2021-01-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirtimesAirtel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Airtel_500', models.CharField(max_length=200)),
                ('Airtel_200', models.CharField(max_length=200)),
                ('Airtel_100', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AirtimesGlo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Glo_500', models.CharField(max_length=200)),
                ('Glo_200', models.CharField(max_length=200)),
                ('Glo_100', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AirtimesMtn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Mtn_500', models.CharField(max_length=200)),
                ('Mtn_200', models.CharField(max_length=200)),
                ('Mtn_100', models.CharField(max_length=200)),
            ],
        ),
    ]
