# Generated by Django 4.1.7 on 2023-04-01 08:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('udpdated_at', models.DateTimeField(verbose_name='Updated At')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('status', models.CharField(choices=[('IP', 'In-Progress'), ('CP', 'Completed')], default='UD', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('udpdated_at', models.DateTimeField(verbose_name='Updated At')),
                ('comment', models.CharField(max_length=255, verbose_name='Comments')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task', to='todo_task.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
