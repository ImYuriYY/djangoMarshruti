from django.urls import path, include, re_path
from .views import *

post_urls = [
    path('top/', top, name='top'),
    path('last/', last, name='last'),
    path('', all, name='all'),
]

urlpatterns = [
    path('', main, name='home'),
    path('posts/', include(post_urls)),
    path('about/', about, name="about"),
    path('contacts/', contacts, name="contacts"),
    path('details/', details, name="details"),
    path('access/', access, name="access"),
    path('set/', set, name="set"),
    path('get/', get, name="get"),
    path('json/', json, name='json'),
    re_path(r'^', error_404, name="error"),
]