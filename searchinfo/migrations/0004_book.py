# Generated by Django 3.1 on 2020-09-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchinfo', '0003_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitsl_name', models.CharField(max_length=100)),
                ('booking_type', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=20)),
            ],
        ),
    ]
