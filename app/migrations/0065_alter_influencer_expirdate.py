# Generated by Django 4.1.7 on 2023-03-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0064_influencer_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='expirDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
