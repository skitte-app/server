# Generated by Django 3.2.8 on 2022-01-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skit', '0004_alter_skit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='skit',
            name='textInImage',
            field=models.TextField(blank=True, null=True),
        ),
    ]
