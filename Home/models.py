from django.db import models
from django.db.models import Q
class std(models.Model):
    name=models.CharField(max_length=250)

class Category(models.Model):
    name=models.CharField(max_length=20,default=12345)

    def __str__(self):
        return self.name
    
    @staticmethod
    def getCategory():
        return Category.objects.all()
    
    
    
    
    
class Customer(models.Model):
    name=models.CharField(max_length=100,default="name")
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=60)
    address=models.CharField(max_length=150)

    @staticmethod
    def getCustomerByemail(emailid):
        return Customer.objects.get(email = emailid) 
    


   

class Product(models.Model):
    pname =models.CharField(max_length=20)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE,default=12345)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='uploads/products')

    @staticmethod
    def getProductbyId(catId):
        return Product.objects.filter(cat=catId)
    @staticmethod
    
    def getProductbyPId(id):
        return Product.objects.filter(id__in=id)


    @staticmethod
    def getProductbyPrice(val1,val2):
        return Product.objects.filter(price__range=[val1,val2])
             
class order(models.Model):
    custid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    prodid=models.ForeignKey(Product,on_delete=models.CASCADE)
    amount=models.IntegerField(max_length=120)

            
           
            
    