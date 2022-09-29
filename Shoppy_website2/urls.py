from django.urls import path
from Shoppy_website2 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Productview.as_view(), name='product_viwes'),
    path('add_cart/', views.Add_Cart, name='add_cart'),
    path('show_cart/', views.Show_Cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('my_account/', views.my_account, name='my_account'),
    path('logout/', views.Logout, name='logout'),
    path('product_details/<int:pk>', views.Product_details_Views.as_view(), name='product_details'),
    # path('delete_iteam/<int:id>', views.delete_iteam, name='delete_iteam'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
