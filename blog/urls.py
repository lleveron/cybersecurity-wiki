from django.urls import path
from . import views
from .views import PostHomeView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostReferencesView, PostGalleryView, UserPostListView, UserListView

urlpatterns = [
    path('', PostHomeView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('articles/', PostListView.as_view(), name='blog-articles'),
    path('articles/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('articles/new/', PostCreateView.as_view(), name='post-create'),
    path('articles/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('articles/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('references/', PostReferencesView.as_view(), name='blog-references'),
    path('gallery/', PostGalleryView.as_view(), name='blog-gallery'),
    path('team/', UserListView.as_view(), name='blog-team'),
]

