# Generated by Django 4.2.7 on 2023-11-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_department_alter_product_details_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
            ],
        ),
    ]