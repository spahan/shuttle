# Generated by Django 2.2.5 on 2019-09-29 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shuttle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='space_number',
            new_name='space',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='title_text',
            new_name='title',
        ),
    ]
