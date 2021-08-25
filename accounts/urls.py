from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # post views
    url (r'^register/$', views.SignUpView.as_view(), name='register'),
    url(r'^login/$', views.CustomLoginView.as_view(), name='login'),
    path ('download', views.csvD, name='download')
]