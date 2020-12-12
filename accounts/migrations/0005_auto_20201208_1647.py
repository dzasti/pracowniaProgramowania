# Generated by Django 3.1.3 on 2020-12-08 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201208_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='dateOfBirth',
            field=models.DateField(default='2019-09-25'),
        ),
        migrations.AddField(
            model_name='users',
            name='id_roli',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='users',
            name='isDeleted',
            field=models.BooleanField(default='True'),
        ),
        migrations.AddField(
            model_name='users',
            name='login',
            field=models.CharField(default='login', max_length=100),
        ),
        migrations.AddField(
            model_name='users',
            name='passwordMd5',
            field=models.CharField(default='haslo', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(default='nazwisko', max_length=100),
        ),
    ]