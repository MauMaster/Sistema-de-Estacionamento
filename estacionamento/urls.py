from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('website.urls')),
    url(r'sistema/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
