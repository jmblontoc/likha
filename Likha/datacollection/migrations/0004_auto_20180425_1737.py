# Generated by Django 2.0.4 on 2018-04-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacollection', '0003_auto_20180424_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childcare',
            name='anemic_children',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='anemic_with_iron',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='diarrhea_cases',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='diarrhea_with_ors',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='given_deworming',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='given_food',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Given complimentary food'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='infants_received_MNP',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Infants who received MNP'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='infants_received_iron',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Infants who received Iron'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='infants_received_vitamin_A',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Infants who received Vitamin A'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='newborn_screening',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='Infant for newborn screening'),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='pneumonia_cases',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='pneumonia_with_tx',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='sick_children',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
