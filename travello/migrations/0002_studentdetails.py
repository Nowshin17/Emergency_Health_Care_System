# Generated by Django 3.1 on 2020-08-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField()),
                ('s_name', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
