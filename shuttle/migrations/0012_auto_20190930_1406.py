# Generated by Django 2.2.5 on 2019-09-30 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0011_driver_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shuttle',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shuttle.Car'),
        ),
    ]