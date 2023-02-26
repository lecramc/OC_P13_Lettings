# Generated by Django 3.0 on 2023-02-23 09:58

from django.db import migrations

def move_lettings(apps, schema_editor):
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')

    objs = []

    fields = (
    'number',
    'street',
    'city',
    'state',
    'zip_code',
    'country_iso_code'
    )

    for old_object in OldLetting.objects.all():
        title = old_object.title
        old_address = old_object.address

        dict_fields = {k: getattr(old_address, k, None) for k in fields}
        address, created = NewAddress.objects.get_or_create(**dict_fields)

        new_letting = NewLetting(title=title, address=address)
        objs.append(new_letting)

    NewLetting.objects.bulk_create(objs)
    
class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0002_auto_20230223_1017'),

    ]

    operations = [
        migrations.RunPython(move_lettings, migrations.RunPython.noop)
    ]

    