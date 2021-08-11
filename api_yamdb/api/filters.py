from django_filters import rest_framework as df_filters
from titles.models import Title


class CharFilterInFilter(df_filters.BaseInFilter, df_filters.CharFilter):
    pass


class TitleFilter(df_filters.FilterSet):
    category = CharFilterInFilter(field_name='category__slug',
                                  lookup_expr='in')
    genre = CharFilterInFilter(field_name='genre__slug', lookup_expr='in')
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    year = df_filters.RangeFilter()

    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year')
