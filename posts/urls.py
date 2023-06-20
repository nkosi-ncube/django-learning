from django.urls import path
from .views import BlogView,BlogDetailView
#pk  is the primary key  as integer -djngo automatically adds incrementing key to our databse models (it adds id)
urlpatterns=[
    path('',BlogView.as_view(),name='home'),
    path('post/<int:pk>',BlogDetailView.as_view(),name='post_detail'),
]