# Generated by Django 3.2.8 on 2021-10-12 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0004_rename_whish_wish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]
