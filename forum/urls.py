from django.urls import path

from forum.views import index, detail

app_name = 'forum'
urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:pk>', detail, name='detail'),
]
