# Generated by Django 4.0.6 on 2022-10-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_mastertable_er'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
