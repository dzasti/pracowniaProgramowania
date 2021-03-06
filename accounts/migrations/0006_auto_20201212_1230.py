# Generated by Django 3.1.3 on 2020-12-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201208_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='id_roli',
        ),
        migrations.AlterField(
            model_name='users',
            name='isDeleted',
            field=models.BooleanField(default='False'),
        ),
    ]
