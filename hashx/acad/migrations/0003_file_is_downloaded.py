# Generated by Django 3.0.8 on 2020-07-26 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0002_auto_20200719_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='is_downloaded',
            field=models.BooleanField(default=False),
        ),
    ]
