# Generated by Django 3.1.1 on 2021-05-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0017_detail_total_deposits'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='r_link',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
