# Generated by Django 3.2.7 on 2021-09-12 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_order_orderdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='id_order',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='id_product',
            new_name='product',
        ),
    ]
