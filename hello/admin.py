from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    search_fields=('title',)
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

    def delete_model(self,request,object):
        pass



admin.site.register(Article,ArticleAdmin)
