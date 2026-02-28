from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class School(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    logo = models.ImageField(upload_to='school_logos/', null=True, blank=True)
    theme_color = models.CharField(max_length=7, default='#000000') # Hex code

    # Default true, schemas will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass
