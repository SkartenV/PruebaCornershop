from django.db import models
import uuid

#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver

# Entidad del Menú del día
class Menu(models.Model):

    Fecha = models.DateField()
    Opcion_1 = models.CharField(max_length=200, null=True, help_text="Ingrese la Opción 1 del Menú")
    Opcion_2 = models.CharField(max_length=200, null=True, help_text="Ingrese la Opción 2 del Menú")
    Opcion_3 = models.CharField(max_length=200, null=True, help_text="Ingrese la Opción 3 del Menú")
    Opcion_4 = models.CharField(max_length=200, null=True, help_text="Ingrese la Opción 4 del Menú")

    #def __str__(self):
    #    return self.Nombre

# Entidad de la Opción del Menú
"""
class Opcion(models.Model):

    Num_Opcion = models.ForeignKey('Menu', on_delete=models.CASCADE)
    Plato_Fondo = models.CharField(max_length=100)
    Ensalada = models.CharField(max_length=100)
    Postre = models.CharField(max_length=100)

    def __str__(self):
        return self.Num_Opcion

# Entidad de los Empleados
class Empleado(models.Model):
    
    #ID_Empleado = models.ForeignKey('Eleccion_Menu', on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (Nombre, Apellido)

# Entidad de Elección de Menú
class Eleccion_Menu(models.Model):

    ID_Empleado = models.ForeignKey('Empleado', default="", on_delete=models.CASCADE)
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Fecha = models.DateField()
    Personalizaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.UUID
"""