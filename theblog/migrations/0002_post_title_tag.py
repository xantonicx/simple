# Generated by Django 5.1.2 on 2024-10-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='default', max_length=255),
        ),
    ]