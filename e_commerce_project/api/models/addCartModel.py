from django.db import models
from .userModel import UserModel
from .productsModel import ProductModel
from .baseModel import BaseModel


class CartModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Products = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return str(self.id)


    class Meta:
        db_table = "Cart_model"
        
    