from django.db.models.expressions import F
from apps.core.models import PaymentPlan
from django.contrib import admin

from .models import PaymentPlan

# Register your models here.

admin.site.register(PaymentPlan)
