# Generated by Django 3.1.3 on 2020-11-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nieruchomość', '0004_auto_20201119_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zrodla',
            old_name='nazwa',
            new_name='nazwa1',
        ),
        migrations.AddField(
            model_name='zrodla',
            name='nazwa2',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
