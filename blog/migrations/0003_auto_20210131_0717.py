# Generated by Django 3.1.5 on 2021-01-31 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210131_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
