# Generated by Django 4.0.6 on 2022-09-28 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='expirDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='influencer',
            name='time',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='cobon',
        ),
    ]