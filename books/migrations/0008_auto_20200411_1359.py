# Generated by Django 3.0.5 on 2020-04-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200410_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
