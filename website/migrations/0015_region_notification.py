# Generated by Django 3.2.12 on 2022-03-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20220227_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='notification',
            field=models.BooleanField(default=False),
        ),
    ]