# Generated by Django 3.2.7 on 2021-09-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_auto_20210916_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ean13_gen',
        ),
        migrations.AlterField(
            model_name='order',
            name='discount_pc',
            field=models.IntegerField(choices=[(0, '0'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%')], default=0, verbose_name='discount_pc'),
        ),
    ]