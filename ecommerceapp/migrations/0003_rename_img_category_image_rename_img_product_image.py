# Generated by Django 4.2.2 on 2023-06-21 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_rename_stack_product_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]