from .models import *
from django_filters import FilterSet, CharFilter, RangeFilter, DateFromToRangeFilter, BaseInFilter


class MyFilter(BaseInFilter, CharFilter):
    pass


class PostFilters(FilterSet):
    # category = MyFilter(field_name='category__category_name', lookup_expr='in')
    date_of_creation = DateFromToRangeFilter()
    # author = MyFilter(field_name='author', lookup_expr='in')

    class Meta:
        model = Post
        fields = ['author', 'date_of_creation']