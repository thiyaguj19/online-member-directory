# Generated by Django 3.2.12 on 2022-02-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20220227_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', help_text='Center Status', max_length=10),
        ),
    ]
