# Generated by Django 4.1.3 on 2022-11-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
