from django.urls import path

from blogs_django.blogs.views import (
    HomeView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailsView,
    AboutUsView,
    ContactUsView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('details/<int:pk>/', PostDetailsView.as_view(), name='post_details'),
    path('about_us', AboutUsView.as_view(), name='about_us'),
    path('contact_us', ContactUsView.as_view(), name='contact_us'),
]
