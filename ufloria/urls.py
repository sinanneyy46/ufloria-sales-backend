from rest_framework.routers import DefaultRouter
from .views import PerfumeViewSet, OrderViewSet, SupplierViewSet, WhatsAppTemplateViewSet, ExportOrdersCSVView
from django.urls import path, include

router = DefaultRouter()
router.register("perfumes", PerfumeViewSet)
router.register("orders", OrderViewSet)
router.register("suppliers", SupplierViewSet)
router.register("template", WhatsAppTemplateViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("orders/export/", ExportOrdersCSVView.as_view(), name="orders-export"),
]
