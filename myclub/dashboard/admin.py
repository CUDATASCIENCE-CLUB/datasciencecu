from django.contrib import admin
from .models import events,thread,replies

admin.site.register(events)
admin.site.register(thread)
admin.site.register(replies)
