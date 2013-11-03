from django.contrib import admin
from companies.models import Company, Contact, Position, ApplyStatus

admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Position)
admin.site.register(ApplyStatus)
