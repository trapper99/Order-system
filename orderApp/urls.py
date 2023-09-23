from django.urls import path
from .views import CreateOrder, CreateShipment

urlpatterns = [
    path('orders/', CreateOrder.as_view()),
    path('shipments/', CreateShipment.as_view()),
]