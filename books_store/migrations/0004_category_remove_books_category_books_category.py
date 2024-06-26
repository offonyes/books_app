# Generated by Django 5.0.4 on 2024-04-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_store', '0003_alter_books_options_remove_books_unique_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='books',
            name='category',
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ManyToManyField(related_name='books', to='books_store.category', verbose_name='Category'),
        ),
    ]
