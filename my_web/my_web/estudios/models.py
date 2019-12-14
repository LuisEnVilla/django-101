from django.contrib.postgres.fields import ArrayField
from django.db import models

class Collector(models.Model):
  status= models.CharField(max_length=60, null=False, blank=True)
  redirect_url= models.CharField(max_length=60, null=False, blank=True)
  disqualification_url= models.CharField(max_length=60, null=False, blank=True)
  response_count= models.IntegerField(blank=True, null=False)
  closed_page_message= models.CharField(max_length=60, null=False, blank=True)
  href= models.CharField(max_length=60, null=False, blank=True)
  close_date= models.DateTimeField(null=False, blank=True)
  display_survey_results= models.BooleanField()
  open= models.BooleanField()
  disqualification_type= models.CharField(max_length=60, null=False, blank=True)
  allow_multiple_responses= models.BooleanField()
  anonymous_type= models.CharField(max_length=60, null=False, blank=True)
  # id= models.CharField(max_length=60, null=False, blank=True)
  name= models.CharField(max_length=60, null=False, blank=True)
  survey_id= models.CharField(max_length=60, null=False, blank=True)
  password_enabled= models.BooleanField()
  date_modified= models.DateTimeField(null=False, blank=True)
  url= models.CharField(max_length=60, null=False, blank=True)
  edit_response_type= models.CharField(max_length=60, null=False, blank=True)
  redirect_type= models.CharField(max_length=60, null=False, blank=True)
  sender_email= models.CharField(max_length=60, null=False, blank=True)
  thank_you_message= models.CharField(max_length=60, null=False, blank=True)
  date_created= models.DateTimeField(null=False, blank=True)
  disqualification_message= models.CharField(max_length=60, null=False, blank=True)
  type= models.CharField(max_length=60, null=False, blank=True)
  response_limit= models.IntegerField(blank=True, null=False)

TYPE_GET_RESPONSE = [
    ('days','DIA'),
    ('hours','HORA'),
    ('weeks','SEMANA'),
    ('minutes','MINUTO'),
    ('months','MES')
]

class Estudio(models.Model):
  name = models.CharField(help_text= "nombre del estudio",max_length=30, null=False, blank=False)
  token = models.CharField(help_text="API SurveyMonkey Token",max_length=120, null=False, blank=False)
  survey = models.CharField(help_text="ID SurveyMonkey",max_length=120, null=False, blank=False)
  message_remainder = ArrayField(models.IntegerField(), blank=False)
  message_sentHour = models.IntegerField(blank=False, null=False)
  default_collector = models.CharField(help_text="Colector inicial", max_length=32,null=False, blank=False)
  get_response_startOf = models.CharField(max_length=32, null=False, blank=False)
  get_response_endOf = models.CharField(max_length=32, null=False, blank=False)
  get_response_type = models.CharField(max_length=15, null=False, blank=False, choices=TYPE_GET_RESPONSE)
  comprehend_atribute = models.CharField(max_length=32, null=False, blank=False)
  comprehend_questions = ArrayField(models.CharField(max_length=32), blank=False)
  comprehend_textByResponse = models.IntegerField(blank=False, null=False)
  email_Source = models.CharField(max_length=240, null=False, blank=False)
  
  def __str__(self):
    return self.name

class Airports(models.Model):
  iata: models.CharField(max_length=5, null=False, blank=False)
  estudio: models.ForeignKey( Estudio, null=False, blank=False, related_name='estudio_airports', on_delete=models.CASCADE)

  def __str__(self):
    return "{} - {}".format(self.name, self.estudio)

class BlackList(models.Model): 
  domain: models.CharField(max_length=32, null=False, blank=False)
  estudio = models.ForeignKey( Estudio, null=False, blank=False, related_name='estudio_blacklist', on_delete=models.CASCADE)

  def __str__(self):
    return "{} - {}".format(self.domain, self.estudio)

TYPE_MESSAGES= [
    ('invite', 'INVITACION'),
    ('reminder', 'RECORDATOPRIO'),
    ('thank_you', 'AGRADECIMIENTO')
]

RECIPIENT_STATUS_MESSAGES= [
    ('has_not_responded', 'SIN RESPONDER'),
    ('partially_responded', 'CON RESPUESTAS PARCIALES'),
    ('completed', 'ENCUESTA COMPLETA'),
    ('responded', 'RESPONDIO')
]

class Messages(models.Model):
  type= models.CharField(max_length=15, null=False, blank=False, choices=TYPE_MESSAGES)
  recipient_status = models.CharField(max_length=15, null=False, blank=False, choices=RECIPIENT_STATUS_MESSAGES)
  subject= models.CharField(max_length=60, null=False,blank=False)
  body_html= models.CharField(max_length=1020, null=False, blank=False)
  embed_first_question = models.BooleanField()
  is_branding_enabled = models.BooleanField()
  estudio = models.ForeignKey(Estudio, null=False, blank=False, related_name='estudio_messages', on_delete=models.CASCADE)

  def __str__(self):
    return "{} - {}".format(self.type, self.estudio)

TYPES_TEMPLATES= [
    ('responded', 'Respuesta de Agradecimiento'),
    ('notification', 'Notificacion')
]

class Template(models.Model):
  type = models.CharField(max_length=15, null=False, blank=False, choices=TYPES_TEMPLATES)
  TemplateName = models.CharField(max_length=32, null=False, blank=False)
  SubjectPart = models.CharField(max_length=32, null=False, blank=False)
  HtmlPart = models.CharField(max_length=1020, null=False, blank=False)
  TextPart = models.CharField(max_length=1020, null=False, blank=False)

  def __str__(self):
    return "{} - {}".format(self.type, self.TemplateName)

class Alerts(models.Model):
  estudio = models.ForeignKey(Estudio, null=False, blank=False, related_name='estudio_alerts', on_delete=models.CASCADE)
  template = models.ForeignKey(Template, null=False, blank=False, related_name='template_alerts', on_delete=models.CASCADE)
  roles = ArrayField(models.CharField(max_length=32), blank=False)
  name = models.CharField(max_length=32, null=False, blank=False)

  def __str__(self):
    return "{} - {}".format(self.type, self.estudio)
