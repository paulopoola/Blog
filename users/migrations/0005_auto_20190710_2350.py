# Generated by Django 2.2.3 on 2019-07-10 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190710_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default=' ', max_length=250),
        ),
    ]
