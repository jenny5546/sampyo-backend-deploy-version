# Generated by Django 3.1.3 on 2020-12-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawimage',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='raw_image'),
        ),
    ]
