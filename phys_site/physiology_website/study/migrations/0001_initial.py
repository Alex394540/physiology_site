# Generated by Django 2.1.2 on 2018-11-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('articles', models.ManyToManyField(to='tasks.Article')),
                ('games', models.ManyToManyField(to='tasks.Game')),
                ('tasks', models.ManyToManyField(to='tasks.Task')),
                ('videos', models.ManyToManyField(to='tasks.Video')),
            ],
        ),
        migrations.AddField(
            model_name='subsection',
            name='themes',
            field=models.ManyToManyField(to='study.Theme'),
        ),
        migrations.AddField(
            model_name='subject',
            name='subsections',
            field=models.ManyToManyField(to='study.Subsection'),
        ),
    ]
