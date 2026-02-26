from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
    CartView,
    CartAddView,
    CartRemoveAllView,
    imageViewFactory,
    ImageViewNoDI,
)
from .utils import ImageLocalStorage

# Create an instance of the image storage
image_storage = ImageLocalStorage()

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("products/", ProductIndexView.as_view(), name="index"),
    path("products/create", ProductCreateView.as_view(), name="form"),
    path("products/<str:id>", ProductShowView.as_view(), name="show"),
    path("cart/", CartView.as_view(), name="cart_index"),
    path("cart/add/<str:product_id>", CartAddView.as_view(), name="cart_add"),
    path("cart/removeAll", CartRemoveAllView.as_view(), name="cart_removeAll"),
    path("image/", imageViewFactory(image_storage).as_view(), name="image_index"),
    path("image/save", imageViewFactory(image_storage).as_view(), name="image_save"),
    path("image-nodi/", ImageViewNoDI.as_view(), name="image-nodi_index"),
    path("image-nodi/save", ImageViewNoDI.as_view(), name="image-nodi_save"),
]
