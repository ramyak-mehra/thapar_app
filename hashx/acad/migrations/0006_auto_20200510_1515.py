# Generated by Django 3.0.5 on 2020-05-10 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0005_auto_20200505_0229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='thumnail_image',
            new_name='thumbnail_image',
        ),
    ]
