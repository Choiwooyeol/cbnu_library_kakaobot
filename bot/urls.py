from django.contrib import admin
from django.conf.urls import url, include
urlpatterns = [
    url(r'^cbnu_lib/',include('cbnu_lib.urls')),
    #path('admin/', admin.site.urls),
]
