# Generated by Django 3.1.7 on 2021-04-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20210402_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('Code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=35)),
                ('Continent', models.CharField(max_length=8)),
                ('Region', models.CharField(max_length=26)),
                ('SurfaceArea', models.FloatField(max_length=10, verbose_name=2)),
                ('Population', models.IntegerField(max_length=11)),
                ('Captital', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('CountryCode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Language', models.CharField(max_length=30)),
                ('IsOfficial', models.BooleanField()),
                ('Percentage', models.FloatField(max_length=20)),
            ],
        ),
    ]