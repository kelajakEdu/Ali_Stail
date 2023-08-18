# Generated by Django 4.2.4 on 2023-08-17 03:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0005_delete_tanlangan'),
        ('userapp', '0003_rename_vilotay_profil_viloyat'),
        ('buyurtma', '0002_alter_savat_vaqt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savat',
            name='vaqt',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 8, 28, 47, 188415)),
        ),
        migrations.CreateModel(
            name='Tanlangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
    ]