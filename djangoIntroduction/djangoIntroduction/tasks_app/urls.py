from django.urls import path
from djangoIntroduction.tasks_app import views

urlpatterns = [
    path('', views.index)
]
