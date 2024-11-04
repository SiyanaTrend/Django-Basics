from django.urls import path

from djangoTemplatesBasics.posts import views

urlpatterns = [
    path('', views.index, name='index')
]