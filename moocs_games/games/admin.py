from django.contrib import admin

# Register your models here.
from django.contrib import admin
from games.models import ROFR_model, JUDO_model

admin.site.register(ROFR_model)
admin.site.register(JUDO_model)