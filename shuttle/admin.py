from django.contrib import admin
from django.core.mail import send_mail
from django.urls import reverse
from .models import Car,Driver,Shuttle,Passenger


class PassengerInline(admin.StackedInline):
    model = Passenger

class ShuttleAdmin(admin.ModelAdmin):
    inlines = [PassengerInline,]

class DriverAdmin(admin.ModelAdmin):
    actions = ['send_infomail']
    def send_infomail(self, request, queryset):
        for driver in queryset:
            send_mail('Your driver info for 36c3', "Ohai,\n\nTo login to the shuttle tool, open {}?{}\nThen you can Signup for shuttles\nIf you want resign from a shuttle or do other changes, visit the LOC Helpdesk\n\n Have a nice day.".format(request.build_absolute_uri(reverse('shuttle:login')), driver.token), 'shuttle@spahan.ch', [driver.mail], fail_silently=False)
    send_infomail.short_description = 'Send Info Mail to driver'
    send_infomail.allowed_permissions = ('view',)

# Register your models here.
admin.site.register(Car)
admin.site.register(Driver,DriverAdmin)
admin.site.register(Shuttle,ShuttleAdmin)
admin.site.register(Passenger)
