from django.urls import path
from .views import CategoryApiView, VariantDetailApiView, ProductDetailApiView


app_name = 'product_api'

urlpatterns = [
    # path('products/', ProductListApiView.as_view(), name = 'products'),
    path('product/<int:pk>', ProductDetailApiView.as_view(), name = 'product'),
    # path('variants/', VariantListApiView.as_view(), name = 'variants'),
    path('variant/<int:pk>', VariantDetailApiView.as_view(), name = 'variant'),
    # path('images/', ImageListApiView.as_view(), name = 'images'),
    # path('options/', OptionListApiView.as_view(), name = 'images'),
    path('categories/', CategoryApiView.as_view(), name = 'categories'),

]