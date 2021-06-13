from django.db import models

# Create your models here.

class PaymentPlan(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    value = models.DecimalField(verbose_name='Value', max_digits=8, decimal_places=2)
    recurring = models.BooleanField(verbose_name='Recurring', default=False)

    class Meta:
        db_table = 'payment_plan'
        verbose_name = 'Payment Plan'
        verbose_name_plural = 'Payment Plans'
        permissions = [('gestionar_payment_plan', 'Puede gestionar Payments Plans')]

    def __str__(self):
        return self.name
