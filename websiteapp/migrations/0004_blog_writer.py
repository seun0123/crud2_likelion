# Generated by Django 4.0.6 on 2022-07-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0003_remove_blog_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
