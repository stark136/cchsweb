# Generated by Django 3.2 on 2021-07-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_image_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='stark', max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='subject',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
