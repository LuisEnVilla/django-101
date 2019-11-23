# Generated by Django 2.2.7 on 2019-11-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('genero', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')], max_length=1)),
                ('hermanos', models.ManyToManyField(related_name='mis_hermanos', to='personas.Persona')),
                ('madre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos_de_la_madre', to='personas.Persona')),
                ('padre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos_del_padre', to='personas.Persona')),
                ('pareja', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mi_pareja', to='personas.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personas.Persona')),
                ('numero_membresia', models.CharField(max_length=10)),
            ],
            bases=('personas.persona',),
        ),
    ]
