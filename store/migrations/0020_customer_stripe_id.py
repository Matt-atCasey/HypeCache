# Generated by Django 2.2.12 on 2020-05-29 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20200529_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]