# Generated by Django 3.2.9 on 2022-01-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_Number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]