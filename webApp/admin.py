from django.contrib import admin
from .models import *
class category_admin(admin.ModelAdmin):
          list_display=('id','category','categoryDescription','status','created_at')
          list_filter=['category']
admin.site.register(Category,category_admin)

class subcategory_admin(admin.ModelAdmin):
        list_display=('id','category','subcategory','subcategoryDescription')
        list_filter=['subcategory']
admin.site.register(SubCategory,subcategory_admin)

class post_admin(admin.ModelAdmin):
        list_display=('id','postTitle','category','subcategory','created_at','image','postdetails','SinglePageTrending','Trending')
        list_display_links=('id','postTitle')
        list_filter=('category','subcategory')
        search_fields=('postTitle','category')
admin.site.register(Posts,post_admin)

class UploadedFileadmin(admin.ModelAdmin):
        list_display=('id','Image')
admin.site.register(UploadedFile,UploadedFileadmin)

class videoFileadmin(admin.ModelAdmin):
        list_display=('id','video')
admin.site.register(videofile,videoFileadmin)

from embed_video.admin import AdminVideoMixin
class videoadmin(AdminVideoMixin,admin.ModelAdmin):
        list_display=('id','title','link','description')
admin.site.register(embvideo,videoadmin)  