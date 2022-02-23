# Generated by Django 3.2.12 on 2022-02-14 23:26

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
                ('level', models.CharField(default='L1', help_text='access level', max_length=2)),
                ('description', models.CharField(blank=True, help_text='Application Role Description', max_length=200)),
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
            name='Metadata',
            fields=[
                ('key', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='OrgRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Organization Role Name', max_length=100)),
                ('description', models.CharField(blank=True, help_text='Organization Role Description', max_length=200)),
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
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('', 'Not Specified')], default='', help_text='Member Gender', max_length=1)),
                ('email', models.EmailField(help_text='Member Email', max_length=30, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(help_text='Member Phone')),
                ('address_1', models.CharField(blank=True, help_text='Member Address_1', max_length=150, null=True)),
                ('address_2', models.CharField(blank=True, help_text='Member Address_2', max_length=150, null=True)),
                ('city', models.CharField(help_text='Member City', max_length=60)),
                ('zip_code', models.CharField(blank=True, help_text='Member zip_code', max_length=10, null=True)),
                ('state', models.CharField(help_text='Member state', max_length=30)),
                ('country', models.CharField(default='USA', help_text='Member country', max_length=30)),
                ('age_group', models.CharField(choices=[('SSE', 'SSE (4 - 18)'), ('YA', 'YA (18 - 40)'), ('Adult', 'Adult (40 +)'), ('', 'Not Specified')], default='', max_length=10)),
                ('member_status', models.IntegerField(choices=[(0, 'Pending_Approval'), (1, 'Approved')], default=0, help_text='member status')),
                ('start_date', models.DateField(blank=True, help_text="Member's OrgRole Start Date", null=True)),
                ('end_date', models.DateField(blank=True, help_text="Member's OrgRole End Date", null=True)),
                ('approle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.approle')),
                ('center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.center')),
                ('orgrole', models.ManyToManyField(help_text='select organization role', to='website.OrgRole')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.region')),
            ],
        ),
        migrations.AddField(
            model_name='center',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.region'),
        ),
    ]
