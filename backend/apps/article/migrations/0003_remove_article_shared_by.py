# Generated by Django 3.1.4 on 2021-01-28 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_shared_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='shared_by',
        ),
    ]