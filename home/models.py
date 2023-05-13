from django.db import models
import datetime
from tinymce.models import HTMLField 


REQUIREMENT=(
    ('rent' , 'rent'),
    ('sale' , 'sale'),
 )
TYPE=(
    ('apartment','apartment'),
    ('bungalow', 'bungalow'),
     ('house','house'),
     ('land' ,'land'),
     ('villa','villa'),
     ('guest','guest'),
     
)
OPTION=(
    ('yes', 'yes'),
    ('no' , 'no'),
)
# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    class Meta:
        db_table="contact"

class properties (models.Model):
    title=models.CharField(max_length=100)
    property_type=models.CharField(max_length=100,choices=TYPE, default="")
    location=models.CharField(max_length=100,default="")
    map_location=models.TextField(default="")
    property_price=models.CharField(max_length=50)
    year_build=models.IntegerField()
    property_for=models.CharField(max_length=30,choices=REQUIREMENT, default="property for")
    description=HTMLField()
    no_of_floors=models.IntegerField(default="no of floors")
    no_of_rooms=models.IntegerField()
    no_of_bathrooms=models.IntegerField()
    area_sqft=models.CharField(max_length=50)
    parking=models.CharField(max_length=100, choices=OPTION, default="parking")
    photo1=models.ImageField(upload_to='properties/')
    photo2=models.ImageField(upload_to='properties/')
    photo3=models.ImageField(upload_to='properties/')
    photo4=models.ImageField(upload_to='properties/')
    contact_person=models.CharField( max_length=100) 
    contact_no=models.CharField( max_length=100)
    class Meta:
        db_table="properties" 
    
# class sell(models.Model):
#     title=models.CharField(max_length=100)
#     property_type=models.CharField(max_length=100,choices=TYPE, default="")
#     location=models.CharField(max_length=100,default="")
#     map_location=models.TextField(default="")
#     property_price=models.FloatField()
#     year_build=models.IntegerField()
#     property_for=models.CharField(max_length=30,choices=REQUIREMENT, default="property for")
#     description=HTMLField()
#     no_of_floors=models.IntegerField(default="no of floors")
#     no_of_rooms=models.IntegerField()
#     no_of_bathrooms=models.IntegerField()
#     area_sqft=models.FloatField()
#     parking=models.CharField(max_length=100, choices=OPTION, default="parking")
#     photo1=models.ImageField(upload_to='properties/')
#     photo2=models.ImageField(upload_to='properties/')
#     photo3=models.ImageField(upload_to='properties/')
#     photo4=models.ImageField(upload_to='properties/')
#     contact_person=models.CharField( max_length=100) 
#     contact_no=models.CharField( max_length=100)
#     class Meta:
#         db_table="property"

class blog(models.Model):
    title=models.CharField(max_length=100)
    description=HTMLField()
    photo=models.ImageField(upload_to='blog/')
    post_by=models.CharField(max_length=50, default="Admin")
    post_on=models.DateField(default=datetime.date.today())
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title
    

class faq(models.Model):
    question=models.TextField()
    Answer=models.TextField()
    class Meta:
        db_table="faq"
    def __str__(self): 
        return self.question 