from django.conf.urls import url

from bot_site import views

urlpatterns = [
    url(r'index/$', views.index, name='site-index'),
    url(r'members/$', views.index, name='site-members'),
    url(r'contact/$', views.index, name='site-contact'),
]
