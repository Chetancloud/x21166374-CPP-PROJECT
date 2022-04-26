from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(Preloan)
admin.site.register(Loan)
admin.site.register(Loan_Items)
admin.site.register(Loan_orders)
admin.site.register(Customer_Address)