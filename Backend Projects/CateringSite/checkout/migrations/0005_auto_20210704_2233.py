# Generated by Django 3.2.4 on 2021-07-04 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0004_alter_dietorder_is_up_to_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_purchase', models.DateTimeField(default=django.utils.timezone.now)),
                ('payment_method', models.TextField()),
                ('to_pay', models.FloatField(null=True)),
                ('surname', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('address_info', models.TextField()),
                ('locality', models.TextField()),
                ('state', models.TextField()),
                ('post_code', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='dietorder',
            name='confirmed_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.ordercheckout'),
        ),
        migrations.DeleteModel(
            name='OrderConfirmed',
        ),
    ]
