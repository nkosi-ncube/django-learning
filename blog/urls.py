from django.urls import path
from .views import BlogHomeView,BlogDetailView,BlogNewPostView,BlogUpdateView,BlogDeleteView


urlpatterns=[
    path('',BlogHomeView.as_view(),name='home'),
    path('post_details/<int:pk>',BlogDetailView.as_view(),name='post_detail'),
    path('post/new/',BlogNewPostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
]