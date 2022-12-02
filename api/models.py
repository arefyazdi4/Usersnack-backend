from django.db import models
from django.core.validators import MinValueValidator
from api.validators import validate_file_size


class Product(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self) -> str:
        return self.name

    objects = models.Manager()


class Extra(Product):
    pass


class Incredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Pizza(Product):
    incredients = models.ManyToManyField(Incredient)
    img = models.ImageField(
        upload_to='api/img',
        validators=[validate_file_size])


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
