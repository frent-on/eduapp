from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^contacto/$', views.contacto_view, name='vista_contacto'),
    url(r'^login/$', views.login_view, name='vista_login'),
    url(r'^logout/$', views.logout_view, name='vista_logout'),
    url(r'^registro/$', views.register_view, name='vista_registro'),
    url(r'^registro1/$', views.registro_vista, name='registro_vista'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


