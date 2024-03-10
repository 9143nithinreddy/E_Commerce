import datetime

from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='ecommerce/ping')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_morrisons = models.IntegerField
    price_sainsburys = models.IntegerField
    price_tesco = models.IntegerField
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This already exists'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class Order(models.Model):
    item = models.ImageField(upload_to='ecommerce/order/pimg', default='')
    product = models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10, default='')
    total = models.CharField(max_length=1000, default='')
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(user_id):
        return Order.objects.filter(user=user_id)

    def __str__(self):
        return self.product  # Assuming `product` contains the name of the product



class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        if hasattr(self, 'product'):
            return f"{self.product} - {self.subject}"
        else:
            return f"{self.subject}"
