from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.post_list_nature, name='post_list'),  # If Find nature list only from method.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
