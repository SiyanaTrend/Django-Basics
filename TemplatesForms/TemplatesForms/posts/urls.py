from django.urls import path

from TemplatesForms.posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dash')
]