from django.contrib import admin
from.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =('title','content','view_count', 'created_at', 'updated_at',)
    search_fields =('title',)