# Generated by Django 3.1.14 on 2022-03-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=12, unique=True)),
                ('homepage', models.CharField(max_length=150)),
                ('telephone', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'db_table': 'center',
            },
        ),
    ]
