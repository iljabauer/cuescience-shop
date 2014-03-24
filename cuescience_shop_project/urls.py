from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "cuescience_shop.views.index_view"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include("cuescience_cart.urls")),
)
