# Generated by Django 3.2 on 2023-04-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda_telefonica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_persona', models.CharField(help_text='Área o Persona', max_length=120)),
                ('numero', models.CharField(help_text='Número o Extensión', max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Agenda_telefonica',
                'ordering': ['area_persona'],
            },
        ),
    ]
