# Generated by Django 2.0.3 on 2018-04-07 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanarchive', '0002_auto_20180407_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fic',
            name='date_created',
        ),
    ]
