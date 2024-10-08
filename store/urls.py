from django.urls import path
from . import views

app_name='store_app'
urlpatterns = [
    path('products',views.shop,name='shop'),
    path('category/<slug:category_slug>/',views.shop,name='products_by_category'),
    path('brand/<slug:brand_slug>/',views.shop,name='products_by_brands'),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_details'),
    path('submit_review/<int:product_id>',views.submit_review,name='submit_review'),

]