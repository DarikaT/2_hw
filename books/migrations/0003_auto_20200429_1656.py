# Generated by Django 3.0.5 on 2020-04-29 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200429_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='created',
        ),
        migrations.RemoveField(
            model_name='books',
            name='updated',
        ),
    ]
