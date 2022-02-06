# Generated by Django 4.0.1 on 2022-02-06 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Application Role Name', max_length=100)),
                ('description', models.CharField(help_text='Application Role Description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Center Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrgRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Organization Role Name', max_length=100)),
                ('description', models.CharField(help_text='Organization Role Description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Region Name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('first_name', models.CharField(help_text='Member First Name', max_length=100)),
                ('last_name', models.CharField(help_text='Member Last Name', max_length=100)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('', 'Not Specified')], default='', help_text='Choose Member Gender', max_length=1)),
                ('email', models.EmailField(help_text='Member Email', max_length=30, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(help_text='Member Phone')),
                ('address', models.CharField(help_text='Member Address', max_length=300, null=True)),
                ('age', models.IntegerField(help_text='Member Age')),
                ('verified', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0, help_text='member status')),
                ('start_date', models.DateField(help_text="Member's OrgRole Start Date")),
                ('end_date', models.DateField(help_text="Member's OrgRole End Date")),
                ('approle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.approle')),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.center')),
                ('orgrole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.orgrole')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.region')),
            ],
        ),
        migrations.AddField(
            model_name='center',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.region'),
        ),
    ]
