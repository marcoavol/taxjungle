# Generated by Django 3.1.4 on 2021-02-01 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_category', '0002_remove_articlecategory_article_category'),
        ('article', '0006_article_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='article_category.articlecategory'),
        ),
    ]
