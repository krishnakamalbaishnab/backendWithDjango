# Generated by Django 5.1.1 on 2024-09-13 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_cart_promotion_order_customer_address_cartitem_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="-"),
            preserve_default=False,
        ),
    ]
