# Generated by Django 2.2.6 on 2020-01-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_text_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(default='', upload_to='images/')),
                ('title', models.CharField(max_length=2000)),
                ('about_me', models.CharField(max_length=1000)),
                ('my_story', models.CharField(max_length=1000)),
                ('about_my_story', models.CharField(max_length=1000)),
                ('who_we', models.CharField(max_length=1000)),
                ('about_who_we', models.CharField(max_length=1000)),
                ('our_mission', models.CharField(max_length=1000)),
                ('about_our', models.CharField(max_length=1000)),
            ],
        ),
    ]