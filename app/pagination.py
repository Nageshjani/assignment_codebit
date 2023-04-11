


#http://127.0.0.1:8000/products/?name=Pro222&category=kj&ordering=-_id

from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

class CustomePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

    
    

