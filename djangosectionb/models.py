from django.db import models

# Create your models here.
class Gender(models.Model):
   gender_id = models.BigAutoField(primary_key=True, blank=False)
   gender = models.CharField(max_length=55, blank=False)
   date_created = models.DateTimeField(auto_now_add=True)
   date_updated = models.DateTimeField(auto_now=True)
   
   class Meta:
       db_table = "genders"