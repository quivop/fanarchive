# Generated by Django 2.1 on 2018-08-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanfic', '0007_auto_20180825_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorgroup',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='group name'),
        ),
    ]