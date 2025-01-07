# Generated by Django 5.1.4 on 2025-01-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('rating', models.FloatField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('room_type', models.CharField(max_length=100)),
            ],
        ),
    ]