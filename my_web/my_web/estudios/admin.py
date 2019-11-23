from django.contrib import admin

from .models import Estudio


class EstudioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Estudio, EstudioAdmin)
