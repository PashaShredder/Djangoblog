from django.db import models


class Post(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=80,
        verbose_name='Title'
    )
    text = models.TextField(
        verbose_name='Text'
    )
    created_date = models.DateTimeField(
        verbose_name='Created Data',
        auto_now_add=True
    )
    publish_date = models.DateTimeField(
        verbose_name='Publish Data',
        auto_now_add=True
    )
    published = models.BooleanField(
        verbose_name='Published',
        default=False
    )

    def __str__(self):
        return f"{self.title}"


class Comments(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Text'
    )
    created_date = models.DateTimeField(
        verbose_name='Created Data',
        auto_now_add=True
    )
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


class Category(models.Model):
    text = models.CharField(
        max_length=80,
        verbose_name='Text'
        )

    def __str__(self):
        return self.text
