# Generated by Django 3.2.9 on 2022-04-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20220403_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]