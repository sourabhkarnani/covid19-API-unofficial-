# Generated by Django 3.0.5 on 2020-04-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_confirmed_cases', models.IntegerField()),
                ('total_death', models.IntegerField()),
                ('total_recovered', models.IntegerField()),
                ('critical_cases', models.IntegerField()),
                ('active_cases', models.IntegerField()),
                ('cases_today', models.IntegerField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(max_length=100)),
                ('country_flag', models.ImageField(blank=True, null=True, upload_to='flags/')),
                ('country_code', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_confirmed_cases', models.IntegerField()),
                ('total_death', models.IntegerField()),
                ('total_recovered', models.IntegerField()),
                ('critical_cases', models.IntegerField()),
                ('active_cases', models.IntegerField()),
                ('cases_today', models.IntegerField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(max_length=50)),
                ('state_code', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
