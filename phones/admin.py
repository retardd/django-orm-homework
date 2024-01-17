from django.contrib import admin

from .models import Mobile


@admin.register(Mobile)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
