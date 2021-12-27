# Generated by Django 3.2.9 on 2021-12-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocietyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=1000)),
                ('number_of_Flats', models.IntegerField()),
                ('number_of_Residents', models.IntegerField()),
                ('number_of_Tenants', models.IntegerField()),
                ('number_of_Wings', models.IntegerField()),
            ],
        ),
    ]
