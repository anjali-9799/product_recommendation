# Generated by Django 4.1.2 on 2022-10-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_product_unit_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PL', 'Placed'), ('IT', 'InTransit'), ('DL', 'Delivered'), ('DA', 'Delayed'), ('RE', 'Returned')], default='PL', max_length=2)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
