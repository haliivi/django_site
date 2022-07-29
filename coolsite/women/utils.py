from django.db.models import Count
from django.core.cache import cache
from women.models import *


class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('get_posts'))
            cache.set('cats', cats, 60)
        if self.request.user.is_authenticated:
            pass
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
