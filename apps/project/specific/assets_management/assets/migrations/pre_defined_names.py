from django.db import migrations

def load_predefined_items(apps, schema_editor):
    PreRegistrationAssetModel = apps.get_model('assets', 'PreRegistrationAssetModel')
    items = [
        "Zimbawes", "Exóticos", "Pergaminos Alemanes", "Alemanes",
        "Dragones", "Micro Lingotes", "Diantes", "Billetes de 1 Millón de Dólares",
        "Agrocheques", "Superchepiches"
    ]
    for name in items:
        PreRegistrationAssetModel.objects.create(name=name)

class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.RunPython(load_predefined_items),
    ]
