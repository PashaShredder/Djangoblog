# Generated by Django 4.1.2 on 2022-10-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, max_length=120, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
