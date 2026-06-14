from django.contrib import admin
from .models import Talebe

# admin.site.register(Talebe)
class OgrenciAdmin(admin.ModelAdmin):
  list_display = ("TC", "AdiSoyadi","Aciklama")
 
admin.site.register(Talebe, OgrenciAdmin)
