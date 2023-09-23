from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, Shipment
from .serializers import OrderSerializer, ShipmentSerializer
from .tasks import send_shipment_email

# Create your views here.
class CreateOrder(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class CreateShipment(CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
    def post(self, request):
        """
        Handle HTTP POST requests.

        Parameters:
            request (Request): The HTTP POST request object.

        Returns:
            Response: The HTTP response object containing serialized data and status.

        Raises:
            ValidationError: If the serializer data is invalid.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        owner_name = serializer.data['owner_name']
        order_name = serializer.data['order']['name']
        owner_email = serializer.data['owner_email']
        send_shipment_email.delay(owner_email, order_name, owner_name)
        return Response(serializer.data, status=status.HTTP_201_CREATED)     