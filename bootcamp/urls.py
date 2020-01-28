from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('instructors/', views.InstructorList.as_view(), name='instructor_list'),
    path('instructors/<int:pk>', views.InstructorDetail.as_view(), name='instructor_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]