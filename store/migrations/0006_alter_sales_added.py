# Generated by Django 3.2.9 on 2021-11-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_sales_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]