# Generated by Django 3.0.7 on 2020-06-18 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='resident',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resident', to='qr_app.Resident'),
        ),
    ]
