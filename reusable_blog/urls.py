from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.post_list, name="post_list"),
    url(r"^/$", views.post_list, name="post_list"),
    url(r"^(?P<id>\d+)/$", views.post_detail, name="post_detail"),
    url(r"^popular/$", views.most_pop, name="most_pop"),
    url(r"^popular/(?P<id>\d+)/$", views.popular_detail, name="popular_detail"),
    url(r"^new/$", views.new_post, name="new_post"),
    url(r"^(?P<id>\d+)/edit$", views.edit_post, name="edit")
]
