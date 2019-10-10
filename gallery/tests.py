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
        image = Image.objects.filter(image_name='james').first()
        delete=Image.objects.filter(image_name=image.image_name).delete()
        images=Image.objects.all()
        self.assertTrue(len(images) == 0)         
   
        
