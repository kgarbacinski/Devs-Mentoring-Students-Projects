# Generated by Django 3.2.4 on 2021-07-02 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_dietorder_is_not_up_to_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dietorder',
            old_name='is_not_up_to_date',
            new_name='is_up_to_date',
        ),
    ]
