# Generated by Django 4.2.2 on 2023-06-20 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('company_address', models.CharField(max_length=100)),
                ('company_phone', models.PositiveBigIntegerField()),
                ('pan_vat_no', models.PositiveBigIntegerField()),
                ('company_registered_document', models.ImageField(blank=True, null=True, upload_to='Registered Company')),
                ('pan_vat_registered_document', models.ImageField(upload_to='Pan Vat Registered')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_detail_modified', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
