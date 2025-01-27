from django.contrib import admin
from core.models import gadgets
# Register your models here.

@admin.register(gadgets)
class gadgets(admin.ModelAdmin):
    list_display=['name','status']
