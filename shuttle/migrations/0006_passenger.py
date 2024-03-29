# Generated by Django 2.2.5 on 2019-09-29 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0005_auto_20190929_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=20)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('shuttle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuttle.Shuttle')),
            ],
        ),
    ]
