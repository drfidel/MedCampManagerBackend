"""
    Copyright (C) <2023>  <Dr. Akiyo Fidel>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>


"""
from django.db import models
from django.utils.text import slugify
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'label'
        verbose_name_plural = 'labels'
    
    def __str__(self):
        return self.name

#Item model, for storing different items to be sold
class Product(models.Model):
    title = models.CharField(max_length=100,blank=True)
    manufacturer = models.CharField(max_length=64, blank=True)
    formulation = models.CharField(max_length=100,blank=True)
    strength = models.IntegerField(blank=True, default=0)
    availableqty = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    label = models.ForeignKey(Label,related_name='itemlabels',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]


    def __str__(self):
        return f"{self.title} from {self.manufacturer}"

    def get_price(self):
        return self.price


    def get_absolute_url(self):
        return reverse("core:product", kwargs={'slug': self.slug})


    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={'slug': self.slug})


    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={'slug': self.slug})


class Order(models.Model):
    patient_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    #overwrite save method
    def save(self, *args, **kwargs):

        if not self.id:
            # if object is a new instance and number of units ordered are less then the total number of units in the batch
            # update the total number of units in the batch and save the order
            if self.quantity < self.product.availableqty:
                self.product.availableqty -= self.quantity
                self.product.save()
                super(OrderItem, self).save(*args, **kwargs)
            else:   
                #do not save the order
                return
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
