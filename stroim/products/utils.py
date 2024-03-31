from django.core.paginator import Paginator

PAGE_FOR_LIST = 10


def paginate(request, object_list, products_per_page):
    paginator = Paginator(object_list, products_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
