from rest_framework import pagination


class RESTAPIPagination(pagination.LimitOffsetPagination):
    default_limit   = 2
    max_limit       = 3