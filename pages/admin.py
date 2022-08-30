from django.contrib import admin
from .models import Musician,Issue,Sprint

# Register your models here.


admin.site.register([Musician,Issue,Sprint])
