from django.conf.urls import url

from IT1 import views


urlpatterns = [
       url(r'^$', views.home),
       url(r'^home/$', views.home),
       url(r'^about/$', views.about),
       url(r'^countries/$', views.countries),
       url(r'^africa/$', views.africa),
       url(r'^america/$', views.america),
       url(r'^europe/$', views.europe),
       url(r'^asia/$', views.asia),
       url(r'^australia/$', views.australia)
]
