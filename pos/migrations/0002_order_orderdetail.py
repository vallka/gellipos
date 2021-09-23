# Generated by Django 3.2.7 on 2021-09-12 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, verbose_name='customer_name')),
                ('customer_email', models.CharField(max_length=100, verbose_name='customer_email')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_dt')),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='created_dt')),
                ('discount_pc', models.IntegerField(default=0, verbose_name='discount_pc')),
                ('discount_gbp', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='discount_gbp')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='total')),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Paid'), (-1, 'Cancelled'), (-2, 'Refunded')], default=0, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='quantity')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.order')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos.product')),
            ],
        ),
    ]