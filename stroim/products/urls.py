from django.urls import path

from .import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list', views.products_list, name='products_list'),
    path('product/<int:product_id>/', views.products_detail, name='products_detail'),
    path('product/<int:product_id>/comment/', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/comment-form/', views.comment_form, name='comment_form'),
    path('category_list/<int:category_id>/', views.category_list, name='category_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('product/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/remove_from_cart_profile/', views.remove_from_cart_profile, name='remove_from_cart_profile'),
    path('search/', views.search_view, name='search'),
]
