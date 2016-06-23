from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/(?P<post_id>[0-9]+)/$', views.add_user, name='add'),
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
]