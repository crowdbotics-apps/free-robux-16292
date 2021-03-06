# Generated by Django 2.2.12 on 2020-04-27 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('expiration_date', models.DateTimeField()),
                ('last_transaction', models.DateTimeField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customerwallet_customer', to='task_profile.CustomerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TaskerWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(max_length=254)),
                ('expiration_date', models.DateTimeField()),
                ('last_transaction', models.DateTimeField()),
                ('tasker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='taskerwallet_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_token', models.CharField(max_length=255)),
                ('payment_account', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymentmethod_wallet', to='wallet.CustomerWallet')),
            ],
        ),
    ]
