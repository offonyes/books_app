# Generated by Django 5.0.4 on 2024-04-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='books',
            name='page_count_idx',
        ),
        migrations.AddField(
            model_name='author',
            name='wiki_page',
            field=models.URLField(blank=True, null=True, verbose_name='Wiki Page'),
        ),
    ]
