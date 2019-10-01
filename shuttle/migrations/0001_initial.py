# Generated by Django 2.2.5 on 2019-09-29 12:59

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=20)),
                ('space_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Shuttle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('departure', models.DateTimeField()),
                ('car', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shuttle.Car')),
                ('driver', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shuttle.Driver')),
            ],
        ),
    ]
