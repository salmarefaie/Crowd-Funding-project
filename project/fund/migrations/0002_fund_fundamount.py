# Generated by Django 4.1.5 on 2023-01-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='fundamount',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
