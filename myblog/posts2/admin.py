from django.contrib import admin
from .models import Post2

# Register your models here.

#admin.site.register(Post2)
@admin.register(Post2)
class Post2Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
        "view_count",
        "created_at",
    )
    search_fields = (
        'title',
    )
    