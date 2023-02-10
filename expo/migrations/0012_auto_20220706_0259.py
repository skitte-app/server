# Generated by Django 3.2 on 2022-07-06 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expo', '0011_textz_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textz',
            name='document',
        ),
        migrations.AddField(
            model_name='textz',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paragraph', to='expo.chapter'),
        ),
    ]