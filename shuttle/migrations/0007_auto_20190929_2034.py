# Generated by Django 2.2.5 on 2019-09-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0006_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
