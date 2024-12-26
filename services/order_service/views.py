from rest_framework import viewsets, filters
from rest_framework.response import Response
from .services import OrderService
from .serializers import OrderSerializer
from ..base.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items').all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'vendor__name']
    ordering_fields = ['created_at']
    
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

    def get_queryset(self):
        # Filter orders based on user or vendor
        user = self.request.user
        if user.is_vendor:
            return self.queryset.filter(vendor=user.vendor)
        return self.queryset.filter(user=user)