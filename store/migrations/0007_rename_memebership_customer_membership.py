# Generated by Django 5.1.5 on 2025-02-01 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20250201_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='memebership',
            new_name='membership',
        ),
    ]
