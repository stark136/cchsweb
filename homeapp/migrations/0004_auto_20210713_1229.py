# Generated by Django 3.2 on 2021-07-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_auto_20210713_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('photo', models.ImageField(upload_to='Homeworks')),
            ],
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]
