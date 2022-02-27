# Generated by Django 3.2.12 on 2022-02-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_orgrole_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='address',
            field=models.CharField(blank=True, help_text='Center Address', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='center_type',
            field=models.CharField(default='Center', help_text='Center centerType', max_length=10),
        ),
        migrations.AddField(
            model_name='center',
            name='city',
            field=models.CharField(blank=True, help_text='Center City', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='country',
            field=models.CharField(default='USA', help_text='Center Country', max_length=30),
        ),
        migrations.AddField(
            model_name='center',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, help_text='Center Latitude', max_digits=20),
        ),
        migrations.AddField(
            model_name='center',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, help_text='Center Longitude', max_digits=20),
        ),
        migrations.AddField(
            model_name='center',
            name='phone',
            field=models.BigIntegerField(default=0, help_text='Center Phone'),
        ),
        migrations.AddField(
            model_name='center',
            name='state',
            field=models.CharField(blank=True, help_text='Center State', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='status',
            field=models.CharField(default='Active', help_text='Center Status', max_length=10),
        ),
        migrations.AddField(
            model_name='center',
            name='website',
            field=models.URLField(blank=True, help_text='Center website', null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='zip_code',
            field=models.CharField(blank=True, help_text='Center Zip', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='message',
            field=models.CharField(help_text='Swamis Quotes', max_length=600),
        ),
    ]
