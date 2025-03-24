# Generated by Django 4.2.20 on 2025-03-24 19:07

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_type', models.CharField(max_length=100, null=True)),
                ('completed_at', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('TO DO', 'To do'), ('IN PROGRESS', 'In Progress'), ('DONE', 'Done'), ('FAILED', 'Failed'), ('BACKLOG', 'Backlog')], max_length=100)),
                ('assignee', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
