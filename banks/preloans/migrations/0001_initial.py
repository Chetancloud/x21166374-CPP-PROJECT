# Generated by Django 2.1.15 on 2022-03-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preloan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_name', models.CharField(max_length=200)),
                ('EIR_CODE', models.CharField(max_length=200)),
                ('Cust_name', models.CharField(max_length=200)),
                ('Cust_email', models.CharField(max_length=200)),
                ('Cust_occu', models.CharField(max_length=200)),
                ('Cust_salary', models.IntegerField()),
            ],
        ),
    ]
