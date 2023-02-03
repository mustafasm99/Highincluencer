# Generated by Django 4.0.6 on 2022-09-29 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_brand_shop_shops_woner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='shops',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.shops'),
        ),
        migrations.AddField(
            model_name='offers',
            name='woner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]