# Generated by Django 4.2.7 on 2023-12-12 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_donationcategorymodel'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdonationmodel',
            name='donation_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.donationcategorymodel'),
        ),
    ]
