# Generated by Django 3.0.3 on 2020-03-03 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=100)),
                ('eventdate', models.DateField()),
                ('eventlength', models.DurationField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('agenda', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Event',
            },
        ),
    ]
