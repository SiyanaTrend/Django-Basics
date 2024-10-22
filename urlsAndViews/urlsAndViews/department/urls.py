from urlsAndViews.department import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='home'),
    path('redirect-to-view/', views.redirect_to_view, name='redirect-view'),
    path('softuni/', views.redirect_to_softuni),
    path('int:pk/', views.view_with_int_pk),
    path('<slug:slug>/', views.view_with_slug),
    path('<int:pk>/<slug:slug>/', views.view_with_pk_slug),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.view_with_regex),
    path('<variable>/', views.view_with_name), #matches untill / => dadadf
    path('<path:variable>/', views.view_with_path),  #matches after the / as well => fsfsdf/fsdfsdfsd/fsfs
]