from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    #path('catalog',views.tour_cat, name='tour_cat'),
    path('slug=<slug:slug>/id=<int:id>/',views.tour_detail, name='tourpage'),
    path('id=<int:id>/order', views.OrderCreateView.as_view(), name='order'),
    path('catalog', views.tour_cat, name='tour_cat'),
    path('guide/<int:tour_id>', views.guide_detail, name='guide'),


#/id=<int:id>


]


