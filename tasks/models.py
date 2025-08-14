# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import date
from django.db import models


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
    idanimal = models.AutoField(db_column='idAnimal', primary_key=True)  # Field name made lowercase.
    idunidad = models.ForeignKey('UnidadProductiva', models.DO_NOTHING, db_column='idUnidad', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(max_length=7)
    raza = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=11, blank=True, null=True)
    peso = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    idmadre = models.ForeignKey('self', models.DO_NOTHING, db_column='idMadre', blank=True, null=True)  # Field name made lowercase.
    idpadre = models.ForeignKey('self', models.DO_NOTHING, db_column='idPadre', related_name='animal_idpadre_set', blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=11, blank=True, null=True)

    @property
    def edad(self):
        if not self.fechanacimiento:
            return None

        today = date.today()

        years = today.year - self.fechanacimiento.year
        months = today.month - self.fechanacimiento.month
        days = today.day - self.fechanacimiento.day

        # Ajustar si todavía no ha cumplido el mes en curso
        if days < 0:
            months -= 1

        # Ajustar si todavía no ha cumplido el año en curso
        if months < 0:
            years -= 1
            months += 12

        if years > 0 and months > 0:
            return f"{years} años y {months} meses"
        elif years > 0:
            return f"{years} años"
        elif months > 0:
            return f"{months} meses"
        else:
            return "Menos de un mes"
    
    class Meta:
        managed = False
        db_table = 'animal'


class Animali(models.Model):
    idanimal = models.IntegerField(db_column='idAnimal', primary_key=True)  # Field name made lowercase.
    idpotrero = models.ForeignKey('Potrero', models.DO_NOTHING, db_column='idPotrero', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    peso = models.CharField(max_length=50, blank=True, null=True)
    fechanacimiento = models.DateField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    idmadre = models.ForeignKey('Madrei', models.DO_NOTHING, db_column='idMadre', blank=True, null=True)  # Field name made lowercase.
    idpadre = models.ForeignKey('Padrei', models.DO_NOTHING, db_column='idPadre', blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animali'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    idempleado = models.IntegerField(db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    idhorario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='idHorario', blank=True, null=True)  # Field name made lowercase.
    idfinca = models.ForeignKey('Finca', models.DO_NOTHING, db_column='idFinca', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    puesto = models.CharField(max_length=100, blank=True, null=True)
    fechacontratacion = models.DateField(db_column='fechaContratacion', blank=True, null=True)  # Field name made lowercase.
    salario = models.FloatField(blank=True, null=True)
    idusuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Finca(models.Model):
    idfinca = models.AutoField(db_column='idFinca', primary_key=True)  # Field name made lowercase.
    cedulapropietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='cedulaPropietario', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    hectareas = models.FloatField( null=True, blank=True)
    fuenteagua = models.CharField(db_column='fuenteAgua', max_length=100, blank=True, null=True)  # Field name made lowercase.
    explotacion = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
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


class LoteAvicola(models.Model):
    idlote = models.AutoField(db_column='idLote', primary_key=True)  # Field name made lowercase.
    idunidad = models.ForeignKey('UnidadProductiva', models.DO_NOTHING, db_column='idUnidad', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lote_avicola'


class Madre(models.Model):
    idmadre = models.AutoField(db_column='idMadre', primary_key=True)  # Field name made lowercase.
    idanimal = models.OneToOneField(Animal, models.DO_NOTHING, db_column='idAnimal')  # Field name made lowercase.
    numero_partos = models.IntegerField(blank=True, null=True)
    ultima_fecha_parto = models.DateField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'madre'


class Madrei(models.Model):
    idmadre = models.IntegerField(db_column='idMadre', primary_key=True)  # Field name made lowercase.
    especie = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'madrei'


class Padre(models.Model):
    idpadre = models.AutoField(db_column='idPadre', primary_key=True)  # Field name made lowercase.
    idanimal = models.OneToOneField(Animal, models.DO_NOTHING, db_column='idAnimal')  # Field name made lowercase.
    numero_montas = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'padre'


class Padrei(models.Model):
    idpadre = models.IntegerField(db_column='idPadre', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    especie = models.CharField(max_length=100, blank=True, null=True)
    raza = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'padrei'


class Potrero(models.Model):
    idpotrero = models.AutoField(db_column='idPotrero', primary_key=True)  # Field name made lowercase.
    idfinca = models.ForeignKey(Finca, models.DO_NOTHING, db_column='idFinca', blank=True, null=True)  # Field name made lowercase.
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
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=9)  # Field name made lowercase.
    departamento = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    contactoalterno = models.CharField(db_column='contactoAlterno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=8, blank=True, null=True)
    fotodocumento = models.CharField(db_column='fotoDocumento', max_length=255, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietario'


class Registroalimenticio(models.Model):
    idalimentacion = models.AutoField(db_column='idAlimentacion', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animali, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipoalimento = models.CharField(db_column='tipoAlimento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroalimenticio'


class Registroproduccion(models.Model):
    idproduccion = models.AutoField(db_column='idProduccion', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animali, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipoproducto = models.CharField(db_column='tipoProducto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroproduccion'


class Registroreproduccion(models.Model):
    idreproduccion = models.AutoField(db_column='idReproduccion', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animali, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    tipoevento = models.CharField(db_column='tipoEvento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resultado = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroreproduccion'


class Registrosalud(models.Model):
    idsalud = models.AutoField(db_column='idSalud', primary_key=True)  # Field name made lowercase.
    idanimal = models.ForeignKey(Animali, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
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
    idanimal = models.ForeignKey(Animali, models.DO_NOTHING, db_column='idAnimal', blank=True, null=True)  # Field name made lowercase.
    tipoevento = models.CharField(db_column='tipoEvento', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechaevento = models.DateField(db_column='fechaEvento', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trazabilidad'


class UnidadProductiva(models.Model):
    idunidad = models.AutoField(db_column='idUnidad', primary_key=True)  # Field name made lowercase.
    idfinca = models.ForeignKey(Finca, models.DO_NOTHING, db_column='idFinca', related_name='unidades_productivas')  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    tipounidad = models.CharField(db_column='tipoUnidad', max_length=7)  # Field name made lowercase.
    especie_destinada = models.CharField(max_length=7)
    area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    capacidad_maxima = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fuenteagua = models.CharField(db_column='fuenteAgua', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipopasto = models.CharField(db_column='tipoPasto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipoconstruccion = models.CharField(db_column='tipoConstruccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sistemaventilacion = models.CharField(db_column='sistemaVentilacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sistemaalimentacion = models.CharField(db_column='sistemaAlimentacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    temperaturacontrolada = models.IntegerField(db_column='temperaturaControlada', blank=True, null=True)  # Field name made lowercase.
    iluminacion = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'unidad_productiva'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    contrasena = models.CharField(max_length=100, blank=True, null=True)
    rol = models.CharField(max_length=50, blank=True, null=True)
    idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idempleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
