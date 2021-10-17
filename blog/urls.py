from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<str:blog>', views.show, name='show-blog'),
    path('blog/<str:blog>/comment', views.addcomment, name='addcomment')
]