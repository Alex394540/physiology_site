# Generated by Django 2.1.2 on 2018-12-05 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_auto_20181111_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('bool_answer', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multianswers', models.BooleanField(default=False)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('bool_answer', models.BooleanField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='complexity',
            field=models.IntegerField(choices=[(0, 'Простое задание'), (1, 'Средняя сложность'), (2, 'Сложное задание')], default=0),
        ),
        migrations.AddField(
            model_name='taskresult',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='question',
            name='task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_task', to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_tests', to='tasks.Task'),
        ),
        migrations.AddField(
            model_name='explanation',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Question'),
        ),
    ]
