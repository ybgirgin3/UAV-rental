# Generated by Django 4.2.7 on 2023-11-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_reservation_customer_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
