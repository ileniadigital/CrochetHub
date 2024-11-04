# Generated by Django 5.1.1 on 2024-11-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_patternyarn_pattern_alter_patternyarn_project_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patternyarn',
            name='project',
        ),
        migrations.RemoveField(
            model_name='project',
            name='yarns',
        ),
        migrations.AddField(
            model_name='pattern',
            name='yarns',
            field=models.ManyToManyField(related_name='patterns', through='api.PatternYarn', to='api.yarn'),
        ),
    ]
