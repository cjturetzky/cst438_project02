# Generated by Django 3.2.7 on 2021-10-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistitem',
            old_name='name',
            new_name='wname',
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]