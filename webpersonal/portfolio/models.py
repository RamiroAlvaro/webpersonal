from django.db import models


class Project(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descripción')
    image = models.ImageField('Imagen', upload_to='projects')
    link = models.URLField('Dirección web', blank=True, null=True)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
