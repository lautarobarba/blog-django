# Generated by Django 3.0.6 on 2020-05-31 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('users', '0013_auto_20200531_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='admin',
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='grupo'),
        ),
    ]
