# Generated by Django 3.2 on 2023-04-13 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agenda_telefonica',
            new_name='Agenda',
        ),
        migrations.AlterModelOptions(
            name='agenda',
            options={'ordering': ['area_persona'], 'verbose_name_plural': 'Agenda'},
        ),
    ]
