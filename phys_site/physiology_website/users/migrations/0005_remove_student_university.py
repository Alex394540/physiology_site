# Generated by Django 2.1.2 on 2019-01-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190103_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
    ]
