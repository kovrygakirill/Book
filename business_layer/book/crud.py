from apps.book.models import Book


class BookCRUD:
    @staticmethod
    def create(
            data: dict
    ) -> Book:
        return Book.objects.create(
            **data,
        )
