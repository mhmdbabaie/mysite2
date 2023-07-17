from django.contrib import admin
from blog.models import Post
# Register your models here.




class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'   # Add a date drill-down navigation
    empty_value_display = "-empty-"
    list_display = ('title','author','image','counted_views','status','published_date')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin) 