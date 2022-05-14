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
        max_length=30,
        choices=COURSE_CHOICES,
        default=LOGISTICA,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class Experience(models.Model):
    company = models.CharField(max_length=100, null=True)
    office = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    final_date = models.DateField(null=True)
    description = models.TextField(null=True)
    resumes = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company


