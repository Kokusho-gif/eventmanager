# Generated by Django 3.0.3 on 2020-12-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201224_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/event_image', verbose_name='イベント画像'),
        ),
    ]
