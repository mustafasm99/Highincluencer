# Generated by Django 4.0.6 on 2022-10-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_requests_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='brand',
        ),
        migrations.AddField(
            model_name='requests',
            name='brand',
            field=models.ManyToManyField(to='app.brand'),
        ),
    ]