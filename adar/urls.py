 
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('thedar.urls')),
     
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
     
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header = "GSS DAR registration"
admin.site.site_title = "GSS DAR registration form"
admin.site.index_title ="Welcome to GSS Dar admin Panel"