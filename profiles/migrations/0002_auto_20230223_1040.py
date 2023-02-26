# Generated by Django 3.0 on 2023-02-23 10:40

from django.db import migrations

def move_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    objs = []

    for old_object in OldProfile.objects.all():
        old_favorite_city = old_object.favorite_city
        old_user = old_object.user


        new_letting = NewProfile(user=old_user, favorite_city=old_favorite_city)
        objs.append(new_letting)

    NewProfile.objects.bulk_create(objs)
    
class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0002_auto_20230223_1017'),

    ]

    operations = [migrations.RunPython(move_profiles, migrations.RunPython.noop)]
