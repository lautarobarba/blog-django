# Generated by Django 3.0.6 on 2020-05-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]