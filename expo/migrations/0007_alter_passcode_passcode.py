# Generated by Django 3.2 on 2022-04-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0006_auto_20220409_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passcode',
            name='passcode',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
