# Generated by Django 3.2.4 on 2021-06-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_machine', '0002_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='Coke',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coins',
            name='Pepsi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coins',
            name='Soda',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]