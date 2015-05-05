from django.conf.urls import include, url
from django.contrib import admin
from usuarios import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pretec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registro/$', views.get_registro),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^perfil/$', views.perfil),
]
