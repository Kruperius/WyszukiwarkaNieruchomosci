# Generated by Django 3.1.3 on 2020-11-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nieruchomość', '0013_auto_20201126_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nieruchomosci',
            name='rodzaj_zabudowy',
            field=models.CharField(choices=[('d', 'Dowolny'), ('A', 'Apartamentowiec'), ('B', 'Blok'), ('D', 'Dom'), ('K', 'Kamienica')], max_length=100),
        ),
    ]
