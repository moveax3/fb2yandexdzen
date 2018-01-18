from django.contrib import admin
from .models import FeedPost

@admin.register(FeedPost)
class BookSectionAdmin(admin.ModelAdmin):
    list_display = ('facebook_post_id', 'title', 'is_published', 'date')
    ordering = ('-date',)
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        queryset.update(is_published=True)
    make_published.short_description = "Публиковать в Яндекс.Дзен"

    def make_unpublished(self, requests, queryset):
        queryset.update(is_published=False)
    make_unpublished.short_description = "Не публиковать в Яндекс.Дзен"
