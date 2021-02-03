# Generated by Django 3.1.4 on 2021-01-29 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0004_auto_20210129_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(choices=[(1, 'Choose a Category'), (2, 'Taxes'), (3, 'Renting'), (4, 'Banking'), (5, 'Insurance')], default=1)),
                ('article_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_category', to='article.article')),
            ],
        ),
    ]