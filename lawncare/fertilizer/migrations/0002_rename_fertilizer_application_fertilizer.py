# Generated by Django 4.2.5 on 2023-09-12 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fertilizer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='fertilizer',
            new_name='Fertilizer',
        ),
    ]
