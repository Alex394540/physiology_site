# Generated by Django 2.1.2 on 2019-01-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_student_university'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['group'], name='users_stude_group_i_ab721d_idx'),
        ),
    ]
