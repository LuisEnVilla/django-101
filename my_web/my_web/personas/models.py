from django.db import models

import random

GENERO_CHOICES = [
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO')
]


class Persona(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido_paterno = models.CharField(
        max_length=200, null=False, blank=False)
    fecha_nacimiento = models.DateTimeField(null=False, blank=False)
    genero = models.CharField(max_length=1, null=False,
                              blank=False, choices=GENERO_CHOICES)
    padre = models.ForeignKey('Persona', null=True, blank=False,
                              related_name='hijos_del_padre', on_delete=models.CASCADE)
    madre = models.ForeignKey('Persona', null=True, blank=False,
                              related_name='hijos_de_la_madre', on_delete=models.CASCADE)
    hermanos = models.ManyToManyField(
        'Persona', related_name='mis_hermanos', through='Hermandad')
    pareja = models.OneToOneField('Persona', null=True, blank=False,
                                  on_delete=models.CASCADE, related_name='mi_pareja')

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido_paterno)

    @property
    def tiene_pareja(self):
        # Una funcion que regresa True si la persona tiene pareja
        return self.pareja is not None

    @property
    def tiene_padre(self):
        # Una funcion que regresa True si la persona tiene padre
        return self.padre is not None

    @property
    def tiene_madre(self):
        # Una funcion que regresa True si la persona tiene madre
        return self.madre is not None

    @property
    def tiene_hermanos(self):
        # Una funcion que regresa True si la persona tiene hermanos
        return self.hermanos.all().count() > 0

    # @property
    # def is_member(self):
    #     return Miembro.objects.filter(persona_ptr=self).first() is not None


class Hermandad(models.Model):
    persona_uno = models.ForeignKey(
        Persona, related_name='rel_from_set', on_delete=models.CASCADE)
    persona_dos = models.ForeignKey(
        Persona, related_name='rel_to_set', on_delete=models.CASCADE)

    def __str__(self):
        persona_uno = getattr(self, 'persona_uno', None)
        persona_dos = getattr(self, 'persona_dos', None)
        if persona_uno is not None and persona_dos is not None:
            return "{} es hermano de {}".format(persona_uno, persona_dos)
        else:
            return ""


# class Miembro(Persona):
#     numero_membresia = models.CharField(max_length=10, null=False, blank=False)

#     def __str__(self):
#         nombre_completo = super(Miembro, self).__str__()
#         return "{} - {}".format(nombre_completo, self.numero_membresia)

#     def save(self, *args, **kwargs):
#         numero_membresia = getattr(self, 'numero_membresia', None)
#         if numero_membresia is None or len(numero_membresia.strip()) == 0:
#             numbers = [n for n in range(0, 10)]
#             numero_membresia = ''.join(
#                 [str(random.choice(numbers)) for _ in range(0, 10)])
#             self.numero_membresia = numero_membresia
#         super(Miembro, self).save(*args, **kwargs)

#     @classmethod
#     def enroll_persona(cls, persona=None):
#         if persona is not None:
#             miembro = cls(persona_ptr=persona)
#             for name, value in vars(persona).items():
#                 setattr(miembro, name, value)
#             miembro.save()
#             return miembro
#         return None
