# Generated by Django 2.2.5 on 2019-11-30 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191130_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_products', to='products.Category'),
        ),
    ]
