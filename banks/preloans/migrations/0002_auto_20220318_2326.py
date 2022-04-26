# Generated by Django 2.1.15 on 2022-03-18 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preloans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('Irecode', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_Type', models.CharField(max_length=200)),
                ('Loan_Interest', models.FloatField()),
                ('Duration_in_moths', models.IntegerField()),
                ('Married', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_apply_date', models.DateTimeField(auto_now_add=True)),
                ('Loan_id', models.CharField(max_length=200, null=True)),
                ('preloan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='preloans.Preloan')),
            ],
        ),
        migrations.CreateModel(
            name='Loan_orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_Installment', models.IntegerField(blank=True, default=0, null=True)),
                ('Loan_disburse_date', models.DateTimeField(auto_now_add=True)),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='preloans.Loan')),
                ('loan_items', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='preloans.Loan_Items')),
            ],
        ),
        migrations.AddField(
            model_name='customer_address',
            name='loan_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='preloans.Loan_Items'),
        ),
    ]
