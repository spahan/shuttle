from django.contrib import admin
from .models import Car,Driver,Shuttle,Passenger

class PassengerInline(admin.StackedInline):
    model = Passenger

class ShuttleAdmin(admin.ModelAdmin):
    inlines = [PassengerInline,]

# Register your models here.
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Shuttle,ShuttleAdmin)
admin.site.register(Passenger)
