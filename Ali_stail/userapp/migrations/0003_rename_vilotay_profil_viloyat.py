# Generated by Django 4.2.4 on 2023-08-15 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_rename_davlat_profil_vilotay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='vilotay',
            new_name='viloyat',
        ),
    ]
