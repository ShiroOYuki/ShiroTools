from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls')),
    path('line_stickers/', include('line_stickers.urls')),
    path('exam/', include('exam.urls')),
    path('admin/', admin.site.urls)
]