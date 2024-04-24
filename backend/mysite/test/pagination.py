from rest_framework.pagination import PageNumberPagination


class PaginationSize(PageNumberPagination):
    page_size = 15