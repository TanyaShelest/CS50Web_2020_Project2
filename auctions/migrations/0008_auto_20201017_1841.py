# Generated by Django 3.1.2 on 2020-10-17 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201017_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='start_price',
            new_name='current_price',
        ),
    ]
