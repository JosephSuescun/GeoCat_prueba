from django.contrib import admin
from .models import Municipality, Entity, Dependency, Producer

# Register your models here.

admin.site.register(Municipality)
admin.site.register(Entity)
admin.site.register(Dependency)
admin.site.register(Producer)

