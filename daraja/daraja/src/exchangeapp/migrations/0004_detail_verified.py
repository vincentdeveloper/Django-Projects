# Generated by Django 3.1.1 on 2020-12-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0003_auto_20201229_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
