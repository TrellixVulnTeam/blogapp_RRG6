# Generated by Django 2.2.6 on 2020-01-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200116_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_2',
            field=models.TextField(default=''),
        ),
    ]