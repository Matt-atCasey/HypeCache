# Generated by Django 2.2.12 on 2020-05-29 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20200529_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'get_latest_by': 'date_ordered'},
        ),
    ]
