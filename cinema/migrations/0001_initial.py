# Generated by Django 2.1.7 on 2019-03-21 15:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('plot', models.TextField()),
                ('year', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('runtime', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('background', models.ImageField(upload_to='backgrounds/')),
                ('video', models.URLField(max_length=180)),
            ],
        ),
    ]
