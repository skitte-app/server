# Generated by Django 3.2 on 2022-04-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0005_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passcode', models.CharField(blank=True, max_length=5, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Pass',
        ),
    ]
