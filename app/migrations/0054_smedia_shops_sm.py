# Generated by Django 4.1.3 on 2023-02-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_shops_shiping_shops_shiping2'),
    ]

    operations = [
        migrations.CreateModel(
            name='smedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link', models.URLField()),
                ('icon', models.ImageField(upload_to='storIcons/')),
            ],
        ),
        migrations.AddField(
            model_name='shops',
            name='sm',
            field=models.ManyToManyField(blank=True, to='app.smedia'),
        ),
    ]
