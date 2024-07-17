from django.contrib import admin
from .models import Contact, Membershipplan, Trainer, Enrollment, Gallery,Attendance

# Register your models here.

admin.site.register(Contact)
admin.site.register(Membershipplan)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(Attendance)