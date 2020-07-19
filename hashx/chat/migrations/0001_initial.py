# Generated by Django 3.0.5 on 2020-07-19 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('group', 'group'), ('private', 'private'), ('public', 'public')], max_length=15)),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('image', 'image'), ('text', 'text'), ('audio', 'audio'), ('video', 'video')], default='text', max_length=10)),
                ('content', models.TextField(max_length=256, null=True)),
                ('media', models.FileField(null=True, upload_to='chatmediafile')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('delivered_user', models.ManyToManyField(related_name='delivered_user', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.ChatRoom')),
                ('seen_user', models.ManyToManyField(related_name='seen_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
