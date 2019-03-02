from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^contact/[a-zA-z0-9]*', views.contact, name="contact"),]
