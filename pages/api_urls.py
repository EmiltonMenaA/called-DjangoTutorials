from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroy.as_view(), name='comment_detail'),
]
