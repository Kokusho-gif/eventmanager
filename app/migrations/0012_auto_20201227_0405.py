# Generated by Django 3.0.3 on 2020-12-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201224_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='background',
            field=models.CharField(choices=[('green', 'media/image/backgroundimage/green.jpg'), ('pink', 'media/image/backgroundimage/pink.jpg')], max_length=10),
        ),
    ]