# Generated by Django 5.0.2 on 2024-02-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
