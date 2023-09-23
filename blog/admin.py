from django.contrib import admin
from .models import Post,Category
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Comment
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    #emoty_value_display = '-empty-'
    list_display= ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('status','author')
    ordering = ['-created_date']
    search_fields = ('title','counted_views')
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
        #emoty_value_display = '-empty-'
    list_display= ('name','post','approved','created_date')
    list_filter = ('post','approved')
    ordering = ['-created_date']
    search_fields = ('name','post')
    #summernote_fields = ('content',)



admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)