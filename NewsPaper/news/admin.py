from django.contrib import admin
from .models import Post, Category


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(category='Business')


nullfy_quantity.short_description = 'переместить в категорию бизнес'


class PostAdmin(admin.ModelAdmin):
    list_display = ('dateCreation', 'title', 'category')
    list_filter = ('dateCreation', 'category')
    search_fields = ('title', 'title__name')
    actions = [nullfy_quantity]


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
