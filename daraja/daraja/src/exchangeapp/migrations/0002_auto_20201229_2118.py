# Generated by Django 3.1.1 on 2020-12-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='phone_code',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='detail',
            name='v_code',
            field=models.IntegerField(default=0),
        ),
    ]
