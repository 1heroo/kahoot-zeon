# Generated by Django 4.1 on 2022-09-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['pk'], 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
    ]
