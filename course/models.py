from django.db import models

from django.conf import settings

from django.db.models import signals
from django.template.defaultfilters import slugify

class Course(models.Model):
    name = models.CharField('Nome', max_length=500)
    slug = models.SlugField('Slug', max_length=500, editable=False)
    description = models.TextField('Descrição')
    quantity_classes = models.IntegerField('Quantidade de Aulas')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    name_teacher = models.CharField('Nome do professor', max_length=100)
    level = models.CharField('Nível', max_length=100)
    assessments = models.DecimalField('Avaliação', max_digits=2, decimal_places=1, default=0.0)
    quantity_assessment = models.IntegerField('Quantidade de avaliação', default=0)

    class Meta:
        db_table = 'Course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

class Coment(models.Model):
    coment = models.TextField('Comentário')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coments = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Coment'
        verbose_name = 'Coment'
        verbose_name_plural = 'Coments'

    def __str__(self):
        return self.coment


class Section(models.Model):
    name = models.CharField('Nome da seção', max_length=300)
    sections = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
    
    def __str__(self):
        return self.name


def pre_save_model(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(pre_save_model, sender=Course)


