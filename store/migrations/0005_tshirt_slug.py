# Generated by Django 3.1.4 on 2020-12-21 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201222_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='slug',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
