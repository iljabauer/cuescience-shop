from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^add/(?P<product_id>\d+)', "cuescience_cart.views.add_view"),
    url(r'^remove/(?P<product_id>\d+)', "cuescience_cart.views.remove_view"),
)