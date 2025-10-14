from django.db import models


class Category ( models.Model ) :
    category_id = models.AutoField ( primary_key=True )
    category_name = models.CharField ( max_length=100 )
    description = models.TextField ( blank=True, null=True )
    image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)

    def __str__(self) :
        return self.category_name


class Product ( models.Model ) :
    product_id = models.AutoField ( primary_key=True )
    product_name = models.CharField ( max_length=50 )
    category = models.ForeignKey ( Category, on_delete=models.CASCADE )
    unit_price = models.IntegerField ()
    description = models.TextField ( blank=True, null=True )
    image = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)

    def __str__(self) :
        return self.product_name


class Order ( models.Model ) :
    order_id = models.AutoField ( primary_key=True )
    order_date = models.DateTimeField ( auto_now_add=True )
    required_date = models.DateTimeField ( blank=False, null=False )
    shipped_date = models.DateTimeField ( blank=False, null=False )

    def __str__(self) :
        return str ( self.order_id )


class OrderDetails ( models.Model ) :
    order = models.ForeignKey ( Order, on_delete=models.CASCADE )
    product = models.ForeignKey ( Product, on_delete=models.CASCADE )
    unit_price = models.IntegerField ()
    quantity = models.IntegerField ()
    discount = models.IntegerField ( default=0 )

    def __str__(self) :
        return self.product.__str__ ()