# Generated by Django 4.2.1 on 2023-07-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GC',
            fields=[
                ('no', models.AutoField(db_column='no', primary_key=True, serialize=False)),
                ('date', models.CharField(db_column='date', max_length=255)),
                ('top', models.CharField(db_column='top', max_length=255)),
                ('bottom', models.CharField(db_column='bottom', max_length=255)),
                ('vehicle', models.IntegerField(db_column='vehicle')),
                ('inout', models.IntegerField(db_column='inout')),
            ],
            options={
                'db_table': 'get',
            },
        ),
    ]
