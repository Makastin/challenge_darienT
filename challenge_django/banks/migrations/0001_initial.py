# Generated by Django 4.0.4 on 2022-04-21 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=11, verbose_name='Bank Type')),
            ],
            options={
                'verbose_name': 'BankType',
                'verbose_name_plural': 'BankTypes',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Bank Name')),
                ('address', models.CharField(max_length=150, verbose_name='Bank Address')),
                ('allowed_credit', models.BooleanField(default=False, verbose_name='Allowed Credit')),
                ('bank_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.banktype', verbose_name='Bank Type')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
    ]
