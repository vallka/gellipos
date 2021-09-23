from django.db import models

# Create your models here.
class Product(models.Model):
    id_product = models.IntegerField('id',primary_key=True)
    reference = models.CharField('reference',max_length=100)    
    name  = models.CharField('name',max_length=500)
    price = models.DecimalField('price',max_digits=8, decimal_places=2)
    ean13 = models.TextField('ean13',blank=True,default='')
    quantity = models.IntegerField('quantity',default=0)

    def __str__(self):
        return self.reference + ' | £'+ str(self.price)+ ' | ' + self.ean13

class Order(models.Model):
    customer_name = models.CharField('customer_name',max_length=100)
    customer_email = models.CharField('customer_email',max_length=100)
    created_dt = models.DateTimeField('created_dt',auto_now_add=True, null=True)
    updated_dt = models.DateTimeField('created_dt',auto_now=True, null=True)
    subtotal = models.DecimalField('subtotal',max_digits=8, decimal_places=2,default=0)
    #discount_pc = models.IntegerField('discount_pc',default=0)

    class DiscountPc(models.IntegerChoices):
        NONE = 0, '0'
        PC10 = 10, '10%'
        PC20 = 20, '20%'
        PC30 = 30, '30%'
        PC40 = 40, '40%'
        PC50 = 50, '50%'

    discount_pc = models.IntegerField('discount_pc',default=DiscountPc.NONE,choices=DiscountPc.choices)
    discount_gbp = models.DecimalField('discount_gbp',default=0,max_digits=8, decimal_places=2)
    total = models.DecimalField('total',max_digits=8, decimal_places=2,default=0)

    class Status(models.IntegerChoices):
        NEW = 0
        PAID = 1
        CANCELLED = -1
        REFUNDED = -2

    status = models.IntegerField('Status',default=Status.NEW,choices=Status.choices)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField('quantity',default=1)



