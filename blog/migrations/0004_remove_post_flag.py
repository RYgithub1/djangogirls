# Generated by Django 2.2.24 on 2021-06-11 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='flag',
        ),
    ]
