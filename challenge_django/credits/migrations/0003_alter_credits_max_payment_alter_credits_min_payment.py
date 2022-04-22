# Generated by Django 4.0.4 on 2022-04-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0002_alter_credittype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='max_payment',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Maximun Payment'),
        ),
        migrations.AlterField(
            model_name='credits',
            name='min_payment',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Minimum Payment'),
        ),
    ]
