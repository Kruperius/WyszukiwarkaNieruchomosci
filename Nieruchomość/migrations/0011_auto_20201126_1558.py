# Generated by Django 3.1.3 on 2020-11-26 15:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Nieruchomość', '0010_auto_20201126_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nieruchomosci',
            name='rodzaj',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('D', 'Dowolny'), ('Domy', 'Domy'), ('K', 'Komercyjne'), ('Dz', 'Działki')], default='D', max_length=100),
        ),
    ]
