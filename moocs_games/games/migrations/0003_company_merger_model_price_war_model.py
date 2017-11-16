# Generated by Django 2.0.dev20170912171944 on 2017-09-26 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20170920_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Merger_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_value', models.TextField(default='0')),
                ('input_price', models.TextField(default='0')),
                ('profit', models.TextField(default='0')),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'game_Company_Merger',
            },
        ),
        migrations.CreateModel(
            name='Price_War_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round1_input_price', models.TextField(default='0')),
                ('round1_profit', models.TextField(default='0')),
                ('round1_quantity', models.TextField(default='0')),
                ('round2_input_price', models.TextField(default='0')),
                ('round2_profit', models.TextField(default='0')),
                ('round2_quantity', models.TextField(default='0')),
                ('round3_input_price', models.TextField(default='0')),
                ('round3_profit', models.TextField(default='0')),
                ('round3_quantity', models.TextField(default='0')),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'game_Price_War',
            },
        ),
    ]
