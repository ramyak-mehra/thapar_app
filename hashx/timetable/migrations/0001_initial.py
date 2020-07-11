# Generated by Django 3.0.5 on 2020-07-10 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('building', models.CharField(choices=[('TAN', 'TAN'), ('LP', 'LP'), ('LT', 'LT'), ('A', 'A Block'), ('B', 'B Block'), ('C', 'C Block'), ('D', 'D Block'), ('E', 'E Block'), ('F', 'F Block'), ('G', 'G Block'), ('COS', 'COS'), ('OAT', 'OAT'), ('LIB', 'Library'), ('MEC', 'Mechanical Block'), ('AUDI', 'Auditorium'), ('GH', 'Guest House'), ('SP', 'Sports Ground')], max_length=4)),
                ('room', models.CharField(max_length=10, null=True)),
                ('floor', models.PositiveSmallIntegerField(null=True)),
                ('published', models.BooleanField(default=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimetableBoard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_repetion', models.DateTimeField()),
                ('end_repetition', models.DateTimeField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True)),
                ('admin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('batch', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acad.Batch')),
            ],
            options={
                'verbose_name': 'Timetable',
                'verbose_name_plural': 'Timetables',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Lecture', 'Lecture'), ('Practical', 'Practical'), ('Tutorial', 'Tutorial')], max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(null=True)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('published', models.BooleanField(default=True)),
                ('private', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acad.Course')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='timetable.Location')),
                ('timetableboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.TimetableBoard')),
            ],
        ),
    ]
