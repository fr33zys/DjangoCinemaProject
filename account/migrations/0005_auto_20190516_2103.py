# Generated by Django 2.1.7 on 2019-05-16 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190516_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
