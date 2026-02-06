from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/',views.store,name='products_by_category'),#لازم تكون جنب الريكوست 
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),#لازم تكون جنب الريكوست 
    path('search/',views.search,name='search'),
]
