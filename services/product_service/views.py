from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from services.base.models import Product
from .permissions import ProductPermission
from .serializers import ProductSerializer

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    vendor = filters.NumberFilter(field_name="vendor__id")
    category = filters.NumberFilter(field_name="category__id")

    class Meta:
        model = Product
        fields = ['is_active', 'vendor', 'category']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('vendor', 'category').all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    filterset_class = ProductFilter
    queryset = Product.objects.select_related('vendor').all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProductFilter

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        if hasattr(self.request.user, 'vendor'):
            return qs.filter(vendor=self.request.user.vendor)
        return qs.filter(is_active=True)