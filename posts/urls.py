from django.urls import path
from .views import(
     BlogView,
     BlogDetailView,
     BlogCreateView,
     BlogUpdateView,
     BlogDeleteView)
#pk  is the primary key  as integer -djngo automatically adds incrementing key to our databse models (it adds id)
urlpatterns=[
    path('',BlogView.as_view(),name='home'),
    path('post/<int:pk>',BlogDetailView.as_view(),name='post_detail'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete')
]