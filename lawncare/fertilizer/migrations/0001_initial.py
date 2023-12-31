# Generated by Django 4.2.5 on 2023-09-11 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bag_weight', models.IntegerField(default=0)),
                ('bag_coverage', models.IntegerField(default=0)),
                ('percent_N', models.DecimalField(decimal_places=2, max_digits=4)),
                ('percent_P', models.DecimalField(decimal_places=2, max_digits=4)),
                ('percent_X', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bags_applied', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date_applied', models.DateField()),
                ('fertilizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fertilizer.fertilizer')),
            ],
        ),
    ]
