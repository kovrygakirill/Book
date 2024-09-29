from rest_framework.response import Response


class ErrorResponse(Response):
    def __init__(self, details: str, status: int = 400):
        super(ErrorResponse, self).__init__(data={'detail': details}, status=status)
