from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', "cuescience_cart.views.index_view"),
    url(r'^add/(?P<product_id>\d+)/$', "cuescience_cart.views.add_view"),
    url(r'^remove/(?P<product_id>\d+)/$', "cuescience_cart.views.remove_view"),
    url(r'^update/$', "cuescience_cart.views.update_view"),
)