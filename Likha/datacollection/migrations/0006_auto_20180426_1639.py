# Generated by Django 2.0.4 on 2018-04-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0005_auto_20180426_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flariasis',
            name='cases',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='flariasis',
            name='clinical_rate',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='flariasis',
            name='given_mda',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Number of people given MDA'),
        ),
        migrations.AlterField(
            model_name='flariasis',
            name='mfd',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
