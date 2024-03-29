from django_filters import FilterSet
from .models import Post


# создаём фильтр
class NewsFilter(FilterSet):
    class Meta:
        model = Post

        fields = {
            'header':['icontains'],
            'authorArticle__account': ['exact'],
            'creationTime': ['gt'],
        }