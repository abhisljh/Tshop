from django.contrib import admin
from store.models import Tshirt, Cart, Brand, Color, IdealFor, NeckType, Ocassion, Sleeve, SizeVariant

# Register your models here.

class SizeVariantConfiguration(admin.TabularInline):
    model = SizeVariant

class TshirtConfiguration(admin.ModelAdmin):
    inlines = [SizeVariantConfiguration]
    list_display = ['name','slug']
    #list_editable = ['slug']


admin.site.register(Tshirt , TshirtConfiguration)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
admin.site.register(NeckType)
admin.site.register(Ocassion)
admin.site.register(Sleeve)
admin.site.register(Cart)





