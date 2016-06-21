from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):
    sport = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['sport']