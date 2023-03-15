from django.contrib import admin
from .models import Post,Profile

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['author','time','position']
    list_filter=['author','time']
    search_fields=('author','time')
admin.site.register(Post,PostAdmin)
admin.site.register(Profile)
    