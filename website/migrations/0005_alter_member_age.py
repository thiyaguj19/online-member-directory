# Generated by Django 3.2.12 on 2022-02-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20220207_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(blank=True, help_text='Member Age', max_length=3),
        ),
    ]
