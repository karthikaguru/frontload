from django.db import models

# Create your models here.
class product(models.Model):
    pname=models.CharField(max_length=20,null=True)
    pnumber=models.IntegerField()
   
    def __str__(self):
        return self.pname

class order(models.Model):
    preference=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    ordernumber=models.IntegerField()
    price=models.FloatField(null=True)
    quantity=models.FloatField(null=True)
    gst=models.IntegerField(default=True)
    bill=models.FloatField(null=True)

   