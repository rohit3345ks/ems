# Generated by Django 3.1.4 on 2020-12-31 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]