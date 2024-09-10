from django.db import models

# Create your models here.
class MBook(models.Model):
    Book_Name=models.CharField(max_length=50);
    Author=models.CharField(max_length=50);
    Number=models.CharField(max_length=50);
    Details=models.CharField(max_length=50);
    Photo=models.ImageField(upload_to='images');

    
    def __str__(self):
        return self.Book_Name