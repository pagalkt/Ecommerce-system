# Generated by Django 4.2.2 on 2023-07-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='mobileNo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
