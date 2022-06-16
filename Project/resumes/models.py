from django.conf import settings
from django.db import models
import uuid

# Create your models here.

def resume_image_name(instance, filename):
    return f"{instance.name}-{str(uuid.uuid4())}-{filename}"
    

class Resume(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to=resume_image_name)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    DES_SISTEMAS = 'Desenvolvimento de Sistemas'
    LOGISTICA = 'Logistica'
    COURSE_CHOICES = [
        (DES_SISTEMAS, 'Desenvolvimento de Sistemas'),
        (LOGISTICA, 'Logistica'),
    ]
    course = models.CharField(
        max_length=50,
        choices=COURSE_CHOICES,
        default=LOGISTICA,
    )

    SUBSEQUENTE = 'Subsequente'
    INTEGRADO = 'Integrado'
    MODALITY_CHOICES = [
        (SUBSEQUENTE, 'Subsequente'),
        (INTEGRADO, 'Integrado'),
    ]
    modality = models.CharField(
        max_length=50,
        choices=MODALITY_CHOICES,
        default=INTEGRADO,
    )
    
    CURSANDO = 'Cursando'
    FINALIZADO = 'Finalizado'
    STATUS_CHOICES = [
        (CURSANDO, 'Cursando'),
        (FINALIZADO, 'Finalizado'),
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=CURSANDO,
    )
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Knowledge(models.Model):
    dominant_skills = models.TextField(null=True, blank=True)
    
    NENHUM = 'Nenhum'
    BASICO = 'Basico'
    INTERMEDIARIO = 'Intermediario'
    AVANCADO = 'Avançado'
    ENGLISH_CHOICES = [
        (NENHUM, 'Nenhum'),
        (BASICO, 'Basico'),
        (INTERMEDIARIO, 'Intermediário'),
        (AVANCADO, 'Avançado')
    ]
    english = models.CharField(
        max_length=50,
        choices=ENGLISH_CHOICES,
        default=NENHUM,
    )

    NENHUM = 'Nenhum'
    BASICO = 'Basico'
    INTERMEDIARIO = 'Intermediario'
    AVANCADO = 'Avançado'
    SPANISH_CHOICES = [
        (NENHUM, 'Nenhum'),
        (BASICO, 'Basico'),
        (INTERMEDIARIO, 'Intermediário'),
        (AVANCADO, 'Avançado')
    ]
    spanish = models.CharField(
        max_length=50,
        choices=SPANISH_CHOICES,
        default=NENHUM,
    )

    basics_skills = models.TextField(null=True, blank=True)
    resume_knowledge = models.OneToOneField(Resume, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.name

class Experience(models.Model):
    company = models.CharField(max_length=100, null=True, blank=True)
    office = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    final_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    resume_experience = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company


