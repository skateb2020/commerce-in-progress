# Generated by Django 3.2.5 on 2022-05-23 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_listings_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(decimal_places=2, max_digits=1000000000000)),
                ('listing', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]