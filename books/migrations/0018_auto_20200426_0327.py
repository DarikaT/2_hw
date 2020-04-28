# Generated by Django 3.0.5 on 2020-04-25 21:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20200426_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(400, message='Минимальное количество символов: 400')]),
        ),
    ]
