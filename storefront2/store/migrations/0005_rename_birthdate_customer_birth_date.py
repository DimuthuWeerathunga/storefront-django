# Generated by Django 4.1.2 on 2022-10-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_last_na_2e448d_idx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birthdate',
            new_name='birth_date',
        ),
    ]
