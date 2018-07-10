from django.conf.urls import url
from .import views


app_name = "articles"

urlpatterns = [
    url(r'^$',views.article_list,name="list"),
    url(r'^(?P<slug>[\w_]+)/$',views.article_details,name="detail"),
]
