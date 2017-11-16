from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),   # This line has changed!
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
