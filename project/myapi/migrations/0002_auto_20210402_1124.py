# Generated by Django 3.1.7 on 2021-04-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('ID', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('CountryCode', models.CharField(max_length=3)),
                ('Disctrict', models.CharField(max_length=20)),
                ('Population', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]