from math import ceil
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_pagination(queryset, page, page_size=None):
    try:
        total = queryset.count()
    except:
        total = len(queryset)
    if (page_size is not None):
        page_size = int(page_size)
    else:
        page_size = 10
    if (page is not None):
        page = int(page)
    else:
        page = 1
    total = ceil(total / page_size)
    paginator = Paginator(queryset, page_size)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = []
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        queryset = []

    if not (queryset):
        total = 0

    data = {
        'page_size': page_size,
        'queryset': queryset,
        'total': total
    }
    return data

