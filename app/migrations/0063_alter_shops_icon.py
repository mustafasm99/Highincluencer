# Generated by Django 4.1.3 on 2023-03-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_alter_shops_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='iconeimage/'),
        ),
    ]