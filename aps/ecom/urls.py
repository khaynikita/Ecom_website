from django.urls import path
from .import views
urlpatterns=[
    path("",views.store),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('trial/',views.trial),
    path('update_item/',views.updateItem),
    path('process_order/',views.processOrder),

]