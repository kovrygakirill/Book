from django.urls import path

from api.book.views import (
    BookRetrieveView,
    BookView,
)

urlpatterns = [
    path('', BookView.as_view(), name='create_book'),
    path('<uuid:id>', BookRetrieveView.as_view(), name='get_book'),
]
