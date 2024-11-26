from .baseModel import BaseModel
from django.db import models


class ProductModel(BaseModel):
    product_name = models.CharField(max_length=255, blank=True)
    categories = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255,blank=True)
    description = models.TextField()
    quantity = models.IntegerField(blank=True, null=True)



    def __str__(self) -> str:
        return str(self.id)


    class Meta:
        db_table = "Product_model"
