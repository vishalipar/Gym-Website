from django.contrib import admin
from .models import Contact, Membershipplan, Trainer, Enrollment

# Register your models here.

admin.site.register(Contact)
admin.site.register(Membershipplan)
admin.site.register(Enrollment)
admin.site.register(Trainer)