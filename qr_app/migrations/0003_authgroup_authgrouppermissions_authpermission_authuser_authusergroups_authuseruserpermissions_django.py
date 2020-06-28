# Generated by Django 3.0.6 on 2020-06-11 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0002_auto_20200525_0704'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppApartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'qr_app_apartment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'qr_app_building',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppDevice',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.TextField()),
                ('device_type', models.CharField(max_length=10)),
                ('os', models.CharField(max_length=10)),
                ('version', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'qr_app_device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppEntrancelog',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'qr_app_entrancelog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppFloor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'qr_app_floor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppResident',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.TextField()),
                ('pw', models.TextField()),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('birth_year', models.IntegerField()),
                ('salt', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'qr_app_resident',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'qr_app_room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppVisitor',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.TextField()),
                ('pw', models.TextField()),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField()),
                ('time', models.BigIntegerField()),
                ('visited', models.IntegerField()),
                ('salt', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'qr_app_visitor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppVisitorVisitrequest',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.TextField()),
                ('building_id', models.IntegerField(blank=True, null=True)),
                ('room_id', models.IntegerField(blank=True, null=True)),
                ('visit_purpose', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'qr_app_visitor_visitRequest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QrAppVisitRequestList',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('resident_uid', models.TextField(blank=True, null=True)),
                ('visitor_uid', models.TextField(blank=True, null=True)),
                ('permit', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'qr_app_visit_request_list',
                'managed': False,
            },
        ),
    ]
