from django.db import models
from accounts.models import MyUser

# Create your models here.
class Dish(models.Model):
    
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE,
        null= False,
        blank = False
        )
        
    """ DISH NAME """
    dish_name = models.CharField(
        max_length = 32,
        blank = False,
        default = "Unnamed dish"
        )
    
    """ DISH INFO """
    dish_info = models.TextField(
        max_length = 256,
        blank = False,
        default = "No info available"
        )
        
    """ STORE LOCATION """
    # locations are scaled down to focus on Central Singapore only 
    STORE = [
        ('Bayfront','Bayfront'),
        ('Bugis','Bugis'),
        ('Cecil','Cecil'),
        ('City Hall','City Hall'),
        ('Clifford Pier','Clifford Pier'),
        ('Marina Centre','Marina Centre'),
        ('Maxwell','Maxwell'),
        ('Tanjong Pagar','Tanjong Pagar'),
        ]
    dish_store = models.CharField(
        choices = STORE,
        max_length = 20,
        default = 'Bugis',
        blank = False,
        )

    """ DISH PRICING """
    dish_price = models.FloatField(
        default = 0.00,
        blank = False,
    )
    
    # photo = models.ImageField(
    #     upload_to = 'static/images', 
    #     default = 'static/images/no-default_image.jpg',
    #     null = True,
    #     )
    
    def __str__(self):
        return (self.dish_name)