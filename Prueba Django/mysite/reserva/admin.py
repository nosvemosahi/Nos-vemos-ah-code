from django.contrib import admin

# Register your models here.

from .models import Place
from .models import User
from .models import Review

admin.site.register(Place)
admin.site.register(User)
admin.site.register(Review)