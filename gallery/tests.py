from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    
     # Set up method
    def setUp(self):
        self.image1= Image(image_name = 'James', description ='james image')
            
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1, Image))
        
    # Testing Save Method
    def test_save_method(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
    # Testing delete Method
    def test_delete_method(self):
        self.image1.save_image()
        image = Image.objects.filter(image_name='James').first()
        delete=Image.objects.filter(image_name=image.image_name).delete()
        images=Image.objects.all()
        self.assertTrue(len(images) == 0) 

     # Testing update Method
    def test_update_method(self):
        self.image1.save_image()
        image = Image.objects.filter(image_name='James').first()
        update=Image.objects.filter(id=image.id).update(image_name="stacy")
        updated= Image.objects.filter(image_name="stacy").first()
        self.assertTrue(image.image_name,updated.image_name)    
        
# Location test

class LocationTestClass(TestCase):
    
     # Set up method
    def setUp(self):
        self.location1= Location(location_name = 'kigali')
            
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location1, Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.location1.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
    # Testing delete Method
    def test_delete_method(self):
        self.location1.save_location()
        location = Location.objects.filter(location_name = 'kigali').first()
        delete=Location.objects.filter(location_name=location.location_name).delete()
        locations=Location.objects.all()
        self.assertTrue(len(locations) == 0) 

    
     # Testing update Method
    def test_update_method(self):
        self.location1.save_location()
        location = Location.objects.filter(location_name = 'kigali').first()
        update=Location.objects.filter(id=location.id).update(location_name="kacyiru")
        updated= Location.objects.filter(location_name="kacyiru").first()
        self.assertTrue(location.location_name,updated.location_name)    

# category test
class CategoryTestClass(TestCase):
    
     # Set up method
    def setUp(self):
        self.category1= Category(name = 'Shoes')
            
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category1, Category))
        
    # Testing Save Method
    def test_save_method(self):
        self.category1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
    # Testing delete Method
    def test_delete_method(self):
        self.category1.save_category()
        category = Category.objects.filter(name = 'Shoes').first()
        delete=Category.objects.filter(name=Category.name).delete()
        categories=Category.objects.all()
        self.assertFalse(len(categories) == 0)  

    # Testing update Method
    def test_update_method(self):
        self.category1.save_category()
        category = Category.objects.filter(name = 'Shoes').first()
        update=Category.objects.filter(id=category.id).update(name="Dresses")
        updated= Category.objects.filter(name="Dresses").first()
        self.assertTrue(category.name,updated.name)                        
                               
   
        
