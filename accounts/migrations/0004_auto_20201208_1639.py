# Generated by Django 3.1.3 on 2020-12-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_users_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
