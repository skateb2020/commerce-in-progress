# Generated by Django 3.2.5 on 2022-05-29 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_rename_listing_closelisting_listings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='listing',
            new_name='listings',
        ),
    ]
