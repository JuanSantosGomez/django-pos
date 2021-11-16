# Generated by Django 3.2.9 on 2021-11-16 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSetObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantitydescription', models.CharField(max_length=100)),
                ('inventory_count', models.PositiveIntegerField()),
                ('nickname', models.CharField(max_length=70)),
                ('nickname_check', models.BooleanField(default=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('productset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdataset.productset')),
            ],
        ),
    ]
