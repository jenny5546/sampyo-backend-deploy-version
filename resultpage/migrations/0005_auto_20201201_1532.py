# Generated by Django 3.1.3 on 2020-12-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultpage', '0004_auto_20201201_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawimage',
            name='image_file',
            field=models.FileField(blank=True, null=True, upload_to='raw_image'),
        ),
    ]
