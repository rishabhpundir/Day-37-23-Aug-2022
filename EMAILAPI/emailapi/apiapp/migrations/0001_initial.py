# Generated by Django 4.0.6 on 2022-08-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_address', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
