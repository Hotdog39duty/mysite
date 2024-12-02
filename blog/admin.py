# blog/admin.py
from django.contrib import admin
from .models import Post, Review

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Fields to display in the admin list view
    search_fields = ('title', 'content')  # Fields to allow search functionality
    list_filter = ('created_at', 'author')  # Filters to help you find posts by date or author
    ordering = ('-created_at',)  # Order posts by creation date, newest first

    # Optional customization for the form view in admin
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author')
        }),
    )


admin.site.register(Review)
