# Generated by Django 5.0.4 on 2024-07-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authgym', '0003_rename_selectmembershipplan_membershipplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='DueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='Price',
            field=models.IntegerField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='paymentStatus',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
