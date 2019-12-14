from django import forms

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


class EstudioForm(forms.ModelForm):
  class Meta:
    models = Estudio
    fields = [
      "name",
      "token",
      "survey",
      "message_remainder",
      "message_sentHour",
      "default_collector",
      "get_response_startOf",
      "get_response_endOf",
      "get_response_type",
      "comprehend_atribute",
      "comprehend_questions",
      "comprehend_textByResponse",
      "email_Source"
    ]
  
  def __init__(self, *args, **kwargs):
    super(EstudioForm, self).__init__(*args, **kwargs) 

class CollectorForm(forms.ModelForm):
  class Meta:
    models: Collector
    fields = [
      "status",
      "redirect_url",
      "disqualification_url",
      "response_count",
      "closed_page_message",
      "href",
      "close_date",
      "display_survey_results",
      "open",
      "disqualification_type",
      "allow_multiple_responses",
      "anonymous_type",
      "name",
      "survey_id",
      "password_enabled",
      "date_modified",
      "url",
      "edit_response_type",
      "redirect_type",
      "sender_email",
      "thank_you_message",
      "date_created",
      "disqualification_message",
      "type",
      "response_limit"
    ]
  
  def __init__(self, *args, **kwargs):
    super(CollectorForm, self).__init__(*args, **kwargs)

class AirportsForm(forms.ModelForm):
  class Meta:
    models = Airports
    fields = [
        'iata',
        'estudio'
    ]

  def __init__(self, *args, **kwargs):
    super(AirportsForm, self).__init__(*args, **kwargs)
