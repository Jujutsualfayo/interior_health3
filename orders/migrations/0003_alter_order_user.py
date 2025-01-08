# Generated by Django 5.1.4 on 2025-01-07 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_rename_order_date_order_created_at_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="users.user",
            ),
        ),
    ]