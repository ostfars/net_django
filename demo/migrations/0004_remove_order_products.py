# Generated by Django 4.1.6 on 2023-03-02 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_orderposition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]