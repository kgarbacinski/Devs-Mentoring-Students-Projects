# Generated by Django 3.2.4 on 2021-07-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_rename_is_not_up_to_date_dietorder_is_up_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietorder',
            name='is_up_to_date',
            field=models.BooleanField(default=True),
        ),
    ]
