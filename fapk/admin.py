from django.contrib import admin

# Register your models here.
from .models import usereg,product,doctoreg,drivereg,Cart,pharmacy,Transaction,Appoinment,injury,Feedback
admin.site.register(usereg)
admin.site.register(product)
admin.site.register(doctoreg)
admin.site.register(drivereg)
admin.site.register(Cart)
admin.site.register(Transaction)
admin.site.register(pharmacy)
admin.site.register(Appoinment)
admin.site.register(injury)
admin.site.register(Feedback)