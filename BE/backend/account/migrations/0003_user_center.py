# Generated by Django 3.1.14 on 2022-03-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220321_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='center',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
