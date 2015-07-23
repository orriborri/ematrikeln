from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
        # Examples:
        # url(r'^$', 'medlemsregister.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        url(r'^add_member',views.add_member),
        url(r'^add/(\w+)/$', views.add),
        url(r'^$', views.index)
        ]


urlpatterns += staticfiles_urlpatterns()

