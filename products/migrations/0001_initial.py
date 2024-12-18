# Generated by Django 5.1.3 on 2024-11-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_photo', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product_type', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
