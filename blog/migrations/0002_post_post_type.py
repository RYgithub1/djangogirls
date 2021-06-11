# Generated by Django 2.2.24 on 2021-06-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('lifestyle', 'Lifestyle'), ('anime', 'Anime'), ('nature', 'Nature')], default='lifestyle', max_length=20),
        ),
    ]