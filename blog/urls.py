from django.urls import path
from .views import BlogHomeView,BlogDetailView


urlpatterns=[
    path('',BlogHomeView.as_view(),name='home'),
    path('post_details/<int:pk>',BlogDetailView.as_view(),name='post_detail'),
]