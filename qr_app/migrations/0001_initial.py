# Generated by Django 3.0.6 on 2020-05-25 06:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('device_type', models.CharField(choices=[('mb', '모바일'), ('tl', '테블릿'), ('pc', 'pc')], default='mb', max_length=10)),
                ('os', models.CharField(blank=True, max_length=10)),
                ('version', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.TextField()),
                ('pw', models.TextField()),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('birth_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.DurationField()),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EntranceLog',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visitor_idx', models.ForeignKey(db_column='visitor_idx', on_delete=django.db.models.deletion.DO_NOTHING, to='qr_app.Visitor')),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='qr_app.Building')),
                ('floor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='qr_app.Floor')),
                ('room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='qr_app.Room')),
            ],
        ),
    ]
