from django.contrib import admin
from .models import Inventory, ChangeLog

admin.site.register(Inventory)
admin.site.register(ChangeLog)
