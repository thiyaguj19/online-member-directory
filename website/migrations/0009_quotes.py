# Generated by Django 3.2.12 on 2022-02-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_orgrole_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(help_text='Swamis Quotes', max_length=300)),
                ('cite', models.CharField(default='Citation', max_length=100)),
            ],
        ),
    ]
