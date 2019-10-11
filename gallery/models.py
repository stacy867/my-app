from django.db import models

# Create your models here.



class Location(models.Model):
    location_name = models.CharField(max_length = 50)
    

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()    
               
    def delete_location(self):
        self.delete() 
        
    def update_location(self):
        self.update()     



        
                    

class Category(models.Model):
    
    name= models.CharField(max_length =30)
   
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete() 
        
    def update_category(self):
        self.update()    
        
    def __str__(self):
        return self.name      
    
class Image(models.Model):
    
    image = models.ImageField(upload_to ='images/',null=True)
    image_name= models.CharField(max_length =30)
    description= models.CharField(max_length =30)
    img_location= models.ForeignKey(Location,null=True)
    category= models.ForeignKey(Category)
    
    def __str__(self):
        return self.image_name
    
   
    def save_image(self):
        self.save()
        
    
    def delete_image(self):
        self.delete() 
         
        
    def update_image(self):
        self.update()

    @classmethod
    def get_image_by_id(cls,id):
        certain_image=cls.objects.filter(id=id)
    
    @classmethod
    def search_by_name(cls,category):
        certain_image = cls.objects.filter(category__name=category)
        return certain_image  
    
    @classmethod
    def filter_by_location(cls,location):
        certain_image=cls.objects.filter(img_location__location_name=location)    
        