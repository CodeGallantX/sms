from django.contrib import admin
from .models import FeeStructure, Invoice, Payment, Scholarship, Expense, Budget

admin.site.register(FeeStructure)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Scholarship)
admin.site.register(Expense)
admin.site.register(Budget)
