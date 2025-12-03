from rest_framework import viewsets, permissions
from .models import Perfume, Order, Supplier, WhatsAppTemplate
from .serializers import PerfumeSerializer, OrderSerializer, SupplierSerializer, WhatsAppTemplateSerializer
import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# -----------------------------
# PERFUME VIEWSET
# -----------------------------
class PerfumeViewSet(viewsets.ModelViewSet):
    queryset = Perfume.objects.all().order_by('name')
    serializer_class = PerfumeSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

# -----------------------------
# ORDER VIEWSET
# -----------------------------

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-date')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# SUPPLIER VIEWSET
# -----------------------------
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

# -----------------------------
# WHATSAPP TEMPLATE VIEWSET
# -----------------------------

class WhatsAppTemplateViewSet(viewsets.ModelViewSet):
    queryset = WhatsAppTemplate.objects.all()
    serializer_class = WhatsAppTemplateSerializer


# ufloria/views.py (append)


class ExportOrdersCSVView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Optional query params:
         - perfume (partial name)
         - student (partial name)
         - date (exact yyyy-mm-dd) OR date_from & date_to
         - status (exact)
        """
        qs = Order.objects.select_related('perfume').all().order_by('-date')

        perfume = request.GET.get('perfume')
        if perfume:
            qs = qs.filter(perfume__name__icontains=perfume)

        student = request.GET.get('student')
        if student:
            qs = qs.filter(student_name__icontains=student)

        status = request.GET.get('status')
        if status:
            qs = qs.filter(status__iexact=status)

        date = request.GET.get('date')
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date:
            qs = qs.filter(date=date)
        else:
            if date_from:
                qs = qs.filter(date__gte=date_from)
            if date_to:
                qs = qs.filter(date__lte=date_to)

        # Prepare CSV response
        filename = "ufloria_orders.csv"
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        # header row
        writer.writerow(["ID", "Date", "Student", "Perfume", "Qty_ml", "Price", "Status"])

        for o in qs:
            writer.writerow([
                o.id,
                o.date.isoformat(),
                o.student_name,
                o.perfume.name if o.perfume else "",
                o.qty_ml,
                f"{o.price}",
                o.status,
            ])

        return response
