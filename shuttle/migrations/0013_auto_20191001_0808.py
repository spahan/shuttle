# Generated by Django 2.2.5 on 2019-10-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0012_auto_20190930_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='mail',
            field=models.EmailField(default='hanfi@spahan.ch', max_length=254),
            preserve_default=False,
        ),
    ]