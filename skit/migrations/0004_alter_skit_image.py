# Generated by Django 3.2.8 on 2021-11-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skit', '0003_auto_20211116_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='skitte-images/post/%Y/%m/', verbose_name='Image'),
        ),
    ]