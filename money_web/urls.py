# To change this template, choose Tools | Templates
# and open the template in the editor.
from django.conf.urls.defaults import patterns, url

from money_web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
        # Login / logout.
    url(r'^login/$', views.login_user, name='login_user'),
)