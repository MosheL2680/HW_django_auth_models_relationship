# Generated by Django 4.2.6 on 2023-11-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_product_ctg_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='default.png', upload_to='products/'),
        ),
    ]
