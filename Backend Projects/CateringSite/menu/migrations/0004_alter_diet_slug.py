# Generated by Django 3.2.4 on 2021-07-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_diet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='slug',
            field=models.SlugField(),
        ),
    ]
