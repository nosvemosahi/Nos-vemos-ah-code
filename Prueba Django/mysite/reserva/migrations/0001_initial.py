# Generated by Django 2.2.6 on 2020-02-28 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('zone', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('opening_days', models.CharField(max_length=200)),
                ('aviable_places', models.IntegerField()),
                ('timestamp_place', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_lastname', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
                ('user_timestamp', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
