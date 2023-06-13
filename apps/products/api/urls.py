from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_view import ProductListAPIVIew, ProductCreateAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('indicator/', IndicadorListAPIView.as_view(), name='Indicador'),
    path('product/list/', ProductListAPIVIew.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
]