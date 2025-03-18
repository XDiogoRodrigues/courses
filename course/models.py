from django.db import models

from django.contrib.auth import get_user_model

from django.db.models import signals
from django.template.defaultfilters import slugify

class Coment(models.model):
    coment = models.TextField('Comentário')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'Coment'
        verbose_name = 'Coment'
        verbose_name_plural = 'Coments'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Section(models.Model):
    name = models.CharField('Nome da seção', max_length=300)

    class Meta:
        db_table = 'Section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Nome', max_length=500)
    slug = models.SlugField('Slug', max_length=500, editable=False)
    description = models.TextField('Descrição')
    quantity_classes = models.IntegerField('Quantidade de Aulas')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    name_teacher = models.CharField('Nome do professor', max_length=100)
    level = models.CharField('Nível', max_length=100)
    assessments = models.DecimalField('Avaliação', max_digits=2, decimal_places=1, blank=True)
    quantity_assessment = models.IntegerField('Quantidade de avaliação', blank=True)
    coments = models.ForeignKey(Coment, on_delete=models.CASCADE, blank=True)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


def pre_save_model(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(pre_save_model, sender=Course)


