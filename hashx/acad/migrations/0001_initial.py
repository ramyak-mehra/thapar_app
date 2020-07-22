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
            name='AcademicCalendar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=30)),
                ('name', models.CharField(max_length=256)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('num', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('GR', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Batch',
                'verbose_name_plural': 'Batchs',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('year', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior Year'), ('SR', 'Senior Year')], max_length=2)),
                ('code', models.CharField(blank=True, default=None, max_length=3, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=35, null=True)),
                ('passed_out', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('batch_of', models.IntegerField(choices=[(2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('code', models.CharField(max_length=10)),
                ('course_site', models.URLField()),
                ('credit', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('l', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('t', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('p', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('mst', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('tut_ses', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('lab_proj', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('quiz', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('est', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('syllabus', models.TextField()),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'unique_together': {('name', 'code')},
            },
        ),
        migrations.CreateModel(
            name='FileTags',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('auth_name', models.CharField(max_length=128)),
                ('publisher', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('published', models.BooleanField(default=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acad.Course')),
            ],
            options={
                'verbose_name': 'Textbook',
                'verbose_name_plural': 'Textbooks',
            },
        ),
        migrations.CreateModel(
            name='FirstYearBatch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=1)),
                ('no', models.PositiveSmallIntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('GR', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='academic_File')),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='academic_file_thumbnails')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128)),
                ('about', models.TextField(blank=True, max_length=512, null=True)),
                ('file_id', models.CharField(max_length=100, null=True)),
                ('published', models.BooleanField(default=True)),
                ('admin_starred', models.BooleanField(default=False)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='acad.Batch')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acad.Branch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='acad.Course')),
                ('tags', models.ManyToManyField(to='acad.FileTags')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='acad.FileType')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drivefolder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('drive_id', models.CharField(max_length=33)),
                ('year', models.SmallIntegerField(blank=True, null=True)),
                ('file_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Drive ID',
                'unique_together': {('year', 'drive_id')},
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ManyToManyField(blank=True, default=None, to='acad.Course'),
        ),
        migrations.AddField(
            model_name='batch',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acad.Branch'),
        ),
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together={('code', 'year')},
        ),
    ]
