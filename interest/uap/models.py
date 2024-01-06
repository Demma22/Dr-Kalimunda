from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#models means decription of the space on the database where we store things
#models are python classes


# class Category(models.Model):
#     name = models.CharField(max_length = 50, null = True, blank = True)
# # This method gives a human readable name for the Object of the class which is our Category    
#     def __str__(self):
#         return self.name
    
# #creating rowsand columns
# class Product(models.Model):
# # Here we are connecting product model to Category model 
# # A foreign key is a column in one table that is being referenced in another table   
#     category_name = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

#     item_name = models.CharField(max_length = 50, null = True, blank = True)
#     total_quantity = models.IntegerField(default = 0, null = True, blank = True)
#     issuied_quantity = models.IntegerField(default = 0, null = True, blank = True)
#     received_quantity = models.IntegerField(default = 0, null = True, blank = True)
#     unit_price = models.IntegerField(default = 0, null = True, blank = True)
#     manufacturer = models.CharField(max_length = 50, null = True, blank = True)
#     brand = models.CharField(max_length = 50, null = True, blank = True)

#     def __str__(self):
#         return self.item_name
    
# class Sale(models.Model):
#     #item name, price, date of purchase, purchasers name,quantity, ammount receievved    
#     #CASCADE will remove the child object when the foreign object is deleted
#     item = models.ForeignKey(Product, on_delete = models.CASCADE)
#     quantity = models.IntegerField(default = 0, null = False, blank = True)
#     ammount_received = models.IntegerField(default = 0, null = False, blank = True)
#     issued_to = models.CharField(max_length = 50, null = True, blank = True)
#     unit_price = models.IntegerField(default = 0, null = True, blank = True)
#     date = models.DateTimeField(auto_now_add = True)
#     #user = models.ForeignKey(User,on_delete=models.CASCADE)

# #we calculate the change usng method below
#     def get_total(self):
#         total = self.quantity * self.item.unit_price
#         return int(total)
#     #we calcuate the change using the method below
#     def get_change(self):
#         change = self.get_total() - self.ammount_received
#         return abs(int(change))
#     #we can add as many fields as possible depending onyour prefere
#     def get_vat(self):
#         pass

    
#     def __str__(self):
#         return self.item.item_name