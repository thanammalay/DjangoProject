# Generated by Django 5.1 on 2024-08-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='example'),
            preserve_default=False,
        ),
    ]
