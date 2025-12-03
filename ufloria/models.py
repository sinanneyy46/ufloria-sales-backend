from django.db import models

# -----------------------------
# PERFUME MODEL
# -----------------------------
class Perfume(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)
    price_per_ml = models.DecimalField(max_digits=8, decimal_places=2)
    sample_available = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


# -----------------------------
# ORDER MODEL
# -----------------------------
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ordered', 'Ordered'),
        ('delivered', 'Delivered'),
        ('paid', 'Paid'),
    ]

    student_name = models.CharField(max_length=100)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE, related_name='orders')
    qty_ml = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.perfume.name} ({self.qty_ml}ml)"


# -----------------------------
# SUPPLIER (FATHER)
# -----------------------------
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WhatsAppTemplate(models.Model):
    template_text = models.TextField(default="""
✨ *New Order Request* ✨
───────────────
👤 Student: *{student}*
🌺 Perfume: *{perfume}*
📦 Qty: *{qty} ml*
💵 Price: *₹{price}*
───────────────
> Please confirm to proceed.
""")

    def __str__(self):
        return "WhatsApp Template"
