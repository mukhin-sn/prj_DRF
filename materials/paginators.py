from rest_framework.pagination import PageNumberPagination


class MaterialsPaginator(PageNumberPagination):
    page_size = 1
    max_page_size = 10
    page_query_param = 'page'
