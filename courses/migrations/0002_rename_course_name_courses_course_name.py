# Generated by Django 3.2.5 on 2021-08-22 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='course_name',
            new_name='course_Name',
        ),
    ]
