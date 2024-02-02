# Generated by Django 5.0.1 on 2024-01-17 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantAddress',
            fields=[
                ('merchant_address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.merchant')),
            ],
        ),
    ]
