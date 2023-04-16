# Generated by Django 4.1.7 on 2023-04-16 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_post_category_postcategory_post_postcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postCategory',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='news.category'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]