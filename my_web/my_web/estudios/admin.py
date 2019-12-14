from django.contrib import admin

from .models import (
    Estudio, 
    Collector, 
    Estudio, 
    Airports, 
    BlackList, 
    Messages, 
    Template, 
    Alerts
)

from .forms import (
    EstudioForm,
    CollectorForm,
    AirportsForm
)


class EstudioAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'survey',
        'email_Source',
        'message_remainder'
    ]

    search_fields = [
        'name',
        'email_Source'
    ]

    list_filter = [
        'email_Source'
    ]

    form = EstudioForm


admin.site.register(Estudio, EstudioAdmin)

class CollectorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'survey_id',
        'close_date',
        'date_modified',
        'sender_email'
    ]

    form = CollectorForm

admin.site.register(Collector, CollectorAdmin)

# class AirportsAdmin(admin.ModelAdmin):
#     list_display = [
#         'iata',
#         'estudio'
#     ]

#     form = AirportsForm

# admin.site.register(Airports, AirportsAdmin)
