from django.db import models

class Product(models.Model):
    product_id   = models.AutoField
    product_name = models.CharField(max_length=80)
    product_desc = models.CharField(max_length=400)
    category     = models.CharField(max_length=50, default="")
    subcategory  = models.CharField(max_length=50, default="")
    price        = models.IntegerField(default=0)
    image        = models.ImageField(upload_to="shop/images", default="")
    publish_date = models.DateField()

    def __str__(self):
        return self.product_name
<<<<<<< HEAD

class Contact(models.Model):
    msg_id      = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=50)
    email       = models.CharField(max_length=80, default="")
    phone       = models.CharField(max_length=400, default="")
    desc        = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id    = models.AutoField(primary_key=True)
    items_json  = models.CharField(max_length=5000, default="")
    name        = models.CharField(max_length=255)
    email       = models.CharField(max_length=255)
    address     = models.CharField(max_length=255)
    city        = models.CharField(max_length=255)
    state       = models.CharField(max_length=255)
    zip_code    = models.CharField(max_length=255)
    phone       = models.CharField(max_length=255, default="")


class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:12] + "..."
=======
>>>>>>> 24802ca1dac3961a98947c235dfbc0f60ec727a7
