# Generated by Django 4.0.3 on 2022-03-06 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_slug_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='category/thumb'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, upload_to='category/thumb'),
        ),
    ]