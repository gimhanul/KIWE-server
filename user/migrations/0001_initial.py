# Generated by Django 3.2.6 on 2021-08-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('agree', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('birth', models.DateField()),
                ('phonenumber', models.CharField(max_length=10)),
            ],
        ),
    ]