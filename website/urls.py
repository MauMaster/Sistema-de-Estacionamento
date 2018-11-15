from django.conf.urls import url, include
from .views import home, contato, servicos

urlpatterns = [
    url(r'^$', home, name='website_home'),
    url(r'^contato$', contato, name='website_contato'),
    url(r'^servicos$', servicos, name='website_servicos'),


]