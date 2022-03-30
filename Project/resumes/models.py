from django.db import models
import uuid

# Create your models here.

def upload_image_resume(instance, filename):
    return f"{instance.name}-{str(uuid.uuid4())}-{filename}"
    

class Resume(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    city = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(upload_to=upload_image_resume, blank=False, null=False)
    course = models.CharField(max_length=50, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



