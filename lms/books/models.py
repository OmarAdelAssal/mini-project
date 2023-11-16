from django.db import models

# Create your models here.

class books (models.Model):
    name =models.CharField(max_length=50 )
    body =models.CharField( max_length=500 )
    images=models.ImageField(upload_to='books/images' ,null=True)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_books(cls):
        return cls.objects.all()
    
    def get_image_url(self):
        return f"/media/{self.images}"