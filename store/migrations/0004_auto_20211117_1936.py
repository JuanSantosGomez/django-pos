# Generated by Django 3.2.9 on 2021-11-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211117_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_created=True, editable=False)),
                ('price', models.FloatField(default=0.0, editable=False, null=True)),
                ('quantity', models.PositiveIntegerField(editable=False)),
                ('cart', models.CharField(editable=False, max_length=36)),
                ('subtotal', models.FloatField(default=0, editable=False)),
                ('description', models.TextField(default=' ', editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='sold',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]