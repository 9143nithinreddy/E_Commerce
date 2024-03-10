from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index'),

    path('signup/', views.signup, name='signup'),  # Added trailing slash

    path('accounts/', include('django.contrib.auth.urls')),

    # Add to cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail, name='cart_detail'),

    # Contact page
    path('contact/', views.contact_page, name="contact"),  # Added trailing slash

    # Checkout
    path('checkout/', views.CheckOut, name="checkout"),
    path('administer/', views.administer, name='administer'),
    path('administrate/', views.administrate, name='administrate'),

    # Order Page
    path('order/', views.Your_Order, name='order'),
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
