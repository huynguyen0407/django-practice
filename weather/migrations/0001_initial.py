# Generated by Django 4.0 on 2022-01-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
