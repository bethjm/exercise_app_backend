# Generated by Django 4.2.1 on 2023-11-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_app', '0015_delete_stretch_alter_exercise_equipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cue',
            name='cues',
        ),
        migrations.AddField(
            model_name='cue',
            name='information',
            field=models.CharField(default='Take it slow', max_length=255),
        ),
    ]
