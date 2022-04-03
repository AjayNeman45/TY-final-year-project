# Generated by Django 3.2.9 on 2022-04-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='amount',
        ),
        migrations.AddField(
            model_name='income',
            name='totalCharges',
            field=models.CharField(blank=True, default=2305, max_length=100, verbose_name='Total Charges'),
        ),
        migrations.AlterField(
            model_name='income',
            name='society_Bank_Name',
            field=models.CharField(default='SBI Bank', max_length=200),
        ),
    ]