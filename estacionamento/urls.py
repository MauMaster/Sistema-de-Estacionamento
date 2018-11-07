from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^core/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]
