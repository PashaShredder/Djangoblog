# Generated by Django 4.1.2 on 2022-10-20 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_post_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
