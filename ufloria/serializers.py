from rest_framework import serializers
from .models import Perfume, Order, Supplier, WhatsAppTemplate

# -----------------------------
# PERFUME SERIALIZER
# -----------------------------
class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfume
        fields = '__all__'


# -----------------------------
# ORDER SERIALIZER
# -----------------------------
class OrderSerializer(serializers.ModelSerializer):
    perfume_name = serializers.ReadOnlyField(source='perfume.name')

    class Meta:
        model = Order
        fields = '__all__'


# -----------------------------
# SUPPLIER SERIALIZER
# -----------------------------
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class WhatsAppTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsAppTemplate
        fields = "__all__"
