# Generated by Django 2.1.5 on 2019-07-07 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginRegister', '0002_auto_20190706_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confiremed',
            field=models.BooleanField(default=False),
        ),
    ]
