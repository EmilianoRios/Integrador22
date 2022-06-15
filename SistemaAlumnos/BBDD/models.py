from django.db import models
from .choices import sexo

class Persona(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    genero = models.CharField(max_length=1, choices=sexo, default='M')
    dni = models.IntegerField()
    
    class Meta:
        abstract = True

class Usuario(Persona):
    
    username = models.CharField(max_length=50,verbose_name='username')
    
    def nombreCompleto(self):
        return "{} {}".format(self.nombre,self.apellido)
    
    def __str__(self):
        return self.nombreCompleto()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        ordering = ['apellido', '-nombre']

class Pais(models.Model):
    nombrePais = models.CharField(max_length=50,verbose_name='NombrePais')
    
    def paisNombre(self):
        return "{}".format(self.nombrePais)
    
    def __str__(self):
        return self.paisNombre()
    
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        db_table = 'pais'
        ordering = ['nombrePais']

class Provincia(models.Model):
    nombreProvincia = models.CharField(max_length=50,verbose_name='NombreProvincia')
    codigoPostal = models.IntegerField(verbose_name='CogidoPostal')
    
    def provinciaDatos(self):
        return "{}, {}".format(self.nombreProvincia, self.codigoPostal)
    
    def __str__(self):
        return self.provinciaDatos()
    
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        db_table = 'provincia'
        ordering = ['nombreProvincia','-codigoPostal']

class Localidad(models.Model):
    nombreLocalidad = models.CharField(max_length=50,verbose_name='NombreLocalidad')
    
    def localidadNombre(self):
        return "{}".format(self.nombreLocalidad)
    
    def __str__(self):
        return self.localidadNombre()
    
    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        db_table = 'localidad'
        ordering = ['nombreLocalidad']
    
class Domicilio(models.Model):
    direccion = models.TextField(max_length=100,verbose_name='Direccion')

    persona = models.ForeignKey(Usuario,null=True, blank=True,on_delete=models.CASCADE)
    
    pais = models.ForeignKey(Pais,null=True, blank=True,on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia,null=True, blank=True,on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad,null=True, blank=True,on_delete=models.CASCADE)

    def direccionCompleta(self):
        return "{}, {} {} {} {}".format(self.persona, self.direccion, self.pais, self.provincia, self.localidad)
    
    def __str__(self):
        return self.direccionCompleta()
    
    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'
        db_table = 'domicilio'
        ordering = ['direccion',]

class Contacto(models.Model):
    email = models.CharField(max_length=50,verbose_name='email')
    telefono = models.IntegerField(verbose_name='telefono')
    
    persona = models.ForeignKey(Usuario,null=True, blank=True,on_delete=models.CASCADE)
    
    def contactoDatos(self):
        return "{}, email:{} tfno:{}".format(self.persona, self.email, self.telefono)
    
    def __str__(self):
        return self.contactoDatos()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        db_table = 'contacto'
        ordering = ['persona', '-email']

class Alumno(Usuario):
    anioCursado = models.CharField(max_length=50,verbose_name='anioCursado')
    
    def alumnoDatos(self):
        return "{} {}".format(self.nombre,self.apellido)
    
    def __str__(self):
        return self.alumnoDatos()
    
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        db_table = 'alumno'
        ordering = ['nombre', '-apellido']

class Profesor(Usuario):
    anioDictando = models.CharField(max_length=50,verbose_name='anioDictando')
    
    def profesorDatos(self):
        return "{} {}, años dictando:{}°".format(self.nombre,self.apellido,self.anioDictando)
    
    def __str__(self):
        return self.profesorDatos()
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        db_table = 'profesor'
        ordering = ['nombre', 'apellido', '-anioDictando']


class Universidad(models.Model):
    nombreUniversidad= models.CharField(max_length=100,verbose_name='nombreUniversidad')
    
    def universidadNombre(self):
        return "{}".format(self.nombreUniversidad)
    
    def __str__(self):
        return self.universidadNombre()
    
    class Meta:
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
        db_table = 'universidad'
        ordering = ['nombreUniversidad']

class Sede(models.Model):
    nombreSede= models.CharField(max_length=100,verbose_name='nombreSede')

    universidad = models.ForeignKey(Universidad,null=True, blank=True,on_delete=models.CASCADE)
    
    def sedeNombre(self):
        return "{}, {}".format(self.universidad,self.nombreSede)
    
    def __str__(self):
        return self.sedeNombre()
    
    class Meta:
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        db_table = 'sede'
        ordering = ['universidad','-nombreSede']
    
class Ubicacion(models.Model):
    ubicacion = models.CharField(max_length=100,verbose_name='ubicacion')
    
    sede = models.ForeignKey(Sede,null=True, blank=True,on_delete=models.CASCADE)
    
    def ubicacionSede(self):
        return "{}, {}".format(self.sede,self.ubicacion)
    
    def __str__(self):
        return self.ubicacionSede()
    
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'
        db_table = 'ubicacion'
        ordering = ['sede','-ubicacion']

class Facultad(models.Model):
    nombreFacultad= models.CharField(max_length=100,verbose_name='nombreFacultad')
    
    sede = models.ForeignKey(Sede,null=True, blank=True,on_delete=models.CASCADE)
    
    def facultadNombre(self):
        return "{}, {}".format(self.sede,self.nombreFacultad)
    
    def __str__(self):
        return self.facultadNombre()
    
    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        db_table = 'facultad'
        ordering = ['sede','-nombreFacultad']

class Carrera(models.Model):
    nombreCarrera= models.CharField(max_length=50,verbose_name='nombreCarrera')
    anios= models.CharField(max_length=50,verbose_name='Años')
    
    facultad = models.ForeignKey(Facultad,null=True, blank=True,on_delete=models.CASCADE)
    
    def carreraNombre(self):
        return "{}, {}".format(self.nombreCarrera,self.anios)
    
    def __str__(self):
        return self.carreraNombre()
    
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        db_table = 'carrera'
        ordering = ['nombreCarrera','-anios']

class Materia(models.Model):
    nombreMateria = models.CharField(max_length=50,verbose_name='NombreMateria')
    horario = models.CharField(max_length=100,verbose_name='Horario')
    anio = models.CharField(max_length=50,verbose_name='Año')
    
    carrera = models.ForeignKey(Carrera,null=True, blank=True,on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,null=True, blank=True,on_delete=models.CASCADE)
    
    def materiaNombre(self):
        return "{} {} {}".format(self.carrera,self.nombreMateria,self.profesor)
    
    def __str__(self):
        return self.materiaNombre()
    
    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        db_table = 'materia'
        ordering = ['carrera','-nombreMateria','-profesor']
    
class Nota(models.Model):
    valorNotaTP1 = models.IntegerField(verbose_name='TP1')
    valorNotaTP2 = models.IntegerField(verbose_name='TP2')
    valorNotaTP3 = models.IntegerField(verbose_name='TP3')
    valorNotaTP4 = models.IntegerField(verbose_name='TP4')
    
    valorNotaFinal = models.IntegerField(verbose_name='NotaFinal')
    
    materia = models.ForeignKey(Materia,null=True, blank=True,on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno,null=True, blank=True,on_delete=models.CASCADE)
    
    def notaNotas(self):
        return "{}, {}, Tp1:{}, Tp2:{}, Tp3:{}, Tp4:{}, Nota Final:{}".format(self.materia,self.alumno,self.valorNotaTP1,self.valorNotaTP2,self.valorNotaTP3,self.valorNotaTP4,self.valorNotaFinal)
    
    def __str__(self):
        return self.notaNotas()
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        db_table = 'nota'
        ordering = ['materia','-alumno','-valorNotaTP1','-valorNotaTP2','-valorNotaTP3','-valorNotaTP4','-valorNotaFinal']