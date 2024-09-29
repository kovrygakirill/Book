import uuid

from django.db import models


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    author = models.CharField(  # TODO need table
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Издатель'
    )
    published_date = models.DateField(
        verbose_name='Дата публикации',
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'book'

    def __str__(self):
        return self.title
