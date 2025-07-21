
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User  # Import del modelo auth_user


class Alerta(models.Model):
    idalerta = models.AutoField(db_column='idAlerta', primary_key=True)  # Field name made lowercase.
    idfinca = models.ForeignKey('Finca', models.DO_NOTHING, db_column='idFinca', blank=True, null=True)  # Field name made lowercase.
    tipoalerta = models.CharField(db_column='tipoAlerta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    fechacreacion = models.DateField(db_column='fechaCreacion', blank=True, null=True)  # Field name made lowercase.
    fechalimite = models.DateField(db_column='fechaLimite', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alerta'


class Animal(models.Model):
    idanimal = models.IntegerField(db_column='idAnimal', primary_key=True)  # Field name made lowercase.
    idpotrero = models.ForeignKey('Potrero', models.DO_NOTHING, db_column='idPotrero', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    peso = models.CharField(max_length=50, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    idmadre = models.ForeignKey('Madre', models.DO_NOTHING, db_column='idMadre', blank=True, null=True)  # Field name made lowercase.
    idpadre = models.ForeignKey('Padre', models.DO_NOTHING, db_column='idPadre', blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal'



class Empleado(models.Model):
    idempleado = models.IntegerField(db_column='idEmpleado', primary_key=True)
    idhorario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='idHorario', blank=True, null=True)
    idfinca = models.ForeignKey('Finca', models.DO_NOTHING, db_column='idFinca', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    puesto = models.CharField(max_length=100, blank=True, null=True)
    fechacontratacion = models.DateField(db_column='fechaContratacion', blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)

    # Nuevo: Relación con usuario (auth_user)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, db_column='idUsuario', blank=True, null=True)

    class Meta:
        managed = False  # Porque esta tabla ya existe en tu base de datos
        db_table = 'empleado'


class Finca(models.Model):
    idfinca = models.AutoField(db_column='idFinca', primary_key=True)  # Field name made lowercase.
    cedulapropietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='cedulaPropietario', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.IntegerField(blank=True, null=True)
    longitud = models.IntegerField(blank=True, null=True)
    hectareas = models.IntegerField(blank=True, null=True)
    fuenteagua = models.CharField(db_column='fuenteAgua', max_length=100, blank=True, null=True)  # Field name made lowercase.
    explotacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'finca'


class Horario(models.Model):
    idhorario = models.AutoField(db_column='idHorario', primary_key=True)  # Field name made lowercase.
    diasemana = models.CharField(db_column='diaSemana', max_length=50, blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='horaInicio', blank=True, null=True)  # Field name made lowercase.
    horafin = models.TimeField(db_column='horaFin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horario'


class Inventario(models.Model):
    idinventario = models.AutoField(db_column='idInventario', primary_key=True)  # Field name made lowercase.
    idfinca = models.ForeignKey(Finca, models.DO_NOTHING, db_column='idFinca', blank=True, null=True)  # Field name made lowercase.
    tipoitem = models.CharField(db_column='tipoItem', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    unidadmedida = models.CharField(db_column='unidadMedida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(blank=True, null=True)
    fechaultimaactualizacion = models.DateField(db_column='fechaUltimaActualizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventario'


class Madre(models.Model):
    idmadre = models.IntegerField(db_column='idMadre', primary_key=True)  # Field name made lowercase.
    especie = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'madre'


class MoverGanado(models.Model):
    idmovimiento = models.AutoField(primary_key=True)
    idanimal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    idpotrero_anterior = models.ForeignKey('Potrero', models.DO_NOTHING, db_column='idpotrero_anterior', blank=True, null=True)
    idpotrero_nuevo = models.ForeignKey('Potrero', models.DO_NOTHING, db_column='idpotrero_nuevo', related_name='moverganado_idpotrero_nuevo_set', blank=True, null=True)
    fechaevento = models.DateField(db_column='fechaEvento', blank=True, null=True)  # Field name made lowercase.
    motivo_movimiento = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mover_ganado'


class Padre(models.Model):
    idpadre = models.IntegerField(db_column='idPadre', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    especie = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'padre'


class Potrero(models.Model):
    idpotrero = models.AutoField(db_column='idPotrero', primary_key=True)  # Field name made lowercase.
    idfinca = models.ForeignKey(Finca, models.DO_NOTHING, db_column='idFinca', blank=True, null=True , related_name='potreros')  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    fuenteagua = models.CharField(db_column='fuenteAgua', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipopasto = models.CharField(db_column='tipoPasto', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'potrero'


class Propietario(models.Model):
    cedulapropietario = models.IntegerField(db_column='cedulaPropietario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=13, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietario'


class Registroalimenticio(models.Model):
    idalimentacion = models.AutoField(db_column='idAlimentacion', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipoalimento = models.CharField(db_column='tipoAlimento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroalimenticio'


class Registroproduccion(models.Model):
    idproduccion = models.AutoField(db_column='idProduccion', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipoproducto = models.CharField(db_column='tipoProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroproduccion'


class Registroreproduccion(models.Model):
    idreproduccion = models.AutoField(db_column='idReproduccion', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipoevento = models.CharField(db_column='tipoEvento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resultado = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroreproduccion'


class Registrosalud(models.Model):
    idsalud = models.AutoField(db_column='idSalud', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    tipotratamiento = models.CharField(db_column='tipoTratamiento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    veterinario = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrosalud'


class Trazabilidad(models.Model):
    idtrazabilidad = models.AutoField(db_column='idTrazabilidad', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animal, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    tipoevento = models.CharField(db_column='tipoEvento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechaevento = models.DateField(db_column='fechaEvento', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trazabilidad'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    contrasena = models.CharField(max_length=100, blank=True, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
