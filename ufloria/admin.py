from django.contrib import admin
from .models import Perfume, Order, Supplier, WhatsAppTemplate

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_ml', 'sample_available')
    search_fields = ('name', 'category')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'perfume', 'qty_ml', 'price', 'status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('student_name', 'perfume__name')
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name", "phone")

@admin.register(WhatsAppTemplate)
class WhatsAppTemplateAdmin(admin.ModelAdmin):
    list_display = ("template_text",)