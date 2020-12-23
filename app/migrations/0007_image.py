# Generated by Django 3.0.3 on 2020-12-23 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200320_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200)),
                ('event_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
            ],
        ),
    ]
