from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

class Libro(models.Model):
    titulo=models.CharField(max_length=80)
    autor=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    fechaIngreso=models.DateTimeField()

    def __str__(self):
        return f" Titulo:{(self.titulo)} | Autor:{(self.autor)} | Genero:{(self.genero)} | fechaIngreso:{(self.fechaIngreso.strftime('%d %b, %Y'))}"   ##.strftime('%d %b, %Y')

class Comentario(models.Model): 
    id=models.IntegerField(primary_key=True)
    creador=models.CharField(max_length=30)
    encabezado=models.CharField(max_length=100)
    texto=RichTextUploadingField()
    fechaCreacion=models.DateTimeField()

    def __str__(self):
        return f"{(self.creador)} - {(self.encabezado)}| {(self.fechaCreacion.strftime('%d %b, %Y'))}"

class Avatar(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)