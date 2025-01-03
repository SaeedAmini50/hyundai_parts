from django.db import models
from aminicar.models import Account



class Category(models.Model):
    title = models.CharField(max_length=100,null=False)
    slug = models.SlugField(max_length=150, unique=True)


    def __str__(self):
        return self.title


def get_product_image_filepath(self, filename):
    return 'product/product_images/' + str(self.pk) + '/product_image.png'


def get_default_product_image():
    return "product/product_default_images/default_product_image.png"


class Product(models.Model):
    toman = 800000
    title = models.CharField(max_length=150, unique=True) 
    slug = models.SlugField(max_length=200, unique=True)
    name= models.CharField(max_length=200, null=True) 
    description = models.TextField(blank=True, null=True)
    port = models.CharField(max_length=150, null=False, unique=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(null=False, blank=False)
    mark = models.CharField(max_length=150, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_product_image_filepath, default=get_default_product_image, blank=True, null=True)
    image1 = models.ImageField(upload_to=get_product_image_filepath, default=get_default_product_image, blank=True, null=True)
    image2 = models.ImageField(upload_to=get_product_image_filepath, default=get_default_product_image, blank=True, null=True)
    image3 = models.ImageField(upload_to=get_product_image_filepath, default=get_default_product_image, blank=True, null=True)
    image4 = models.ImageField(upload_to=get_product_image_filepath, default=get_default_product_image, blank=True, null=True)

    @property
    def show_price(self):
        total_price = self.price * self.toman
        rounded_price = round(total_price, -len(str(int(total_price))) + 3)  # رُند کردن به 5 رقم اول
        return f"{int(rounded_price):,}"  # فرمت عدد با کاما

    @property
    def discounted_price(self):
        base_price = self.price * self.toman  # محاسبه قیمت پایه
        rounded_price = round(base_price, -len(str(int(base_price))) + 2)  # رُند کردن به 5 رقم اول
        increased_price = rounded_price * 1.05  # افزودن 5 درصد
        return f"{int(increased_price):,}"  # فرمت عدد با کاما


    def __str__(self):
        return self.title

    
    # Model Save override for upload image
    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(Product, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField(blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product.title



class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    total_price = models.FloatField(blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    tracking_code = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

