# Generated by Django 2.2.7 on 2019-11-23 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_remove_persona_hermanos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hermandad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_dos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to='personas.Persona')),
                ('persona_uno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to='personas.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='hermanos',
            field=models.ManyToManyField(related_name='mis_hermanos', through='personas.Hermandad', to='personas.Persona'),
        ),
    ]