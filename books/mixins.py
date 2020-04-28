from .models import Books
from django.core.exceptions import PermissionDenied
from django.db.models import Q



class DispatchFuncMixin():
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class GetQuerySetMixin():
    def get_queryset(self):
            query_result = self.request.GET.get('search_title')
            if query_result: 
                queryset = Books.objects.filter(
                    Q(title__icontains=query_result) |
                    Q(book__icontains=query_result) 
                )

            else:
                queryset = Books.objects.all()
            return queryset

