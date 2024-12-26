from rest_framework import viewsets
from rest_framework.response import Response
from .services import OrderService
from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        service = OrderService()
        order = service.create_order(
            user=request.user,
            items=request.data['items']
        )
        
        if service.has_errors():
            return Response({'errors': service.errors}, status=400)
            
        return Response(OrderSerializer(order).data, status=201)

    def list(self, request):
        orders = self.get_queryset()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            order = self.get_queryset().get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=404)