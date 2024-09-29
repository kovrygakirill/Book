import logging

from django.db import transaction
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView
)

from api.response import ErrorResponse
from api.book.serializers import BookSerializer
from apps.book.models import Book
from business_layer.book.crud import BookCRUD

logger = logging.getLogger('book')


class BookRetrieveView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = BookSerializer

    def get_object(self):
        return Book.objects.get(
            id=self.kwargs[self.lookup_field],
        )

    def handle_exception(
            self,
            exc,
    ):
        if isinstance(
                exc,
                (Http404, ObjectDoesNotExist),
        ):
            return ErrorResponse('Указанная книга не найдена.')
        return super(
            BookRetrieveView,
            self,
        ).handle_exception(exc)


class BookView(GenericAPIView):
    serializer_class = BookSerializer

    def post(
            self,
            request: Request
    ) -> Response:
        try:
            book_serializer = self.serializer_class(
                data=request.data,
            )
            book_serializer.is_valid(raise_exception=True)
            book_data = book_serializer.validated_data

            with transaction.atomic():
                book_instance = BookCRUD.create(
                    data=book_data
                )
        except Exception as error:
            error_message = str(error) or 'Ошибка при создании заявления книги.'
            logger.error(f'{error_message}')
            return ErrorResponse(error_message)

        return Response(data={'id': book_instance.id})
