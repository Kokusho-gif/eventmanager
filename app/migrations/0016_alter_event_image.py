# Generated by Django 3.2.13 on 2022-04-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='../media/image/backgroundimage/green.jpg', null=True, upload_to='image/event_image', verbose_name='イベント画像'),
        ),
    ]