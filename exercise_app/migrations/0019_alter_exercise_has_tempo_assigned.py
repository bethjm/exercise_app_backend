# Generated by Django 4.2.1 on 2024-02-07 19:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_app', '0018_exercise_can_be_assigned_weight_hold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='has_tempo_assigned',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('eccentric', 'Eccentric'), ('concentric', 'Concentric'), ('isometric', 'Isometric'), ('no_tempo', 'No Tempo'), ('cannot_be_assigned', 'Cannot be assigned a tempo')], default='cannot_be_assigned', max_length=255),
        ),
    ]
