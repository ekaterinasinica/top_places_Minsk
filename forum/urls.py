from django.urls import path

from web.views import index, detail

app_name = 'forum'
urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:pk>', detail, name='detail'),
]