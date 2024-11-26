from django.db import models
from .baseModel import BaseModel
from .userModel import UserModel
from .productsModel import ProductModel
from django.db.models import JSONField

PAYMENT_TYPE = [
    (1,"CARD"),
    (2,"CASH ON DELIVERY"),
]

PAYMENT_STATUS = [
    (1,"NOT DONE"),
    (2,"PAYMENT COMPLETE"),
    (3,"ON HOLD"),
]


class PaymentModel(BaseModel):
    user = models.ForeignKey(UserModel,on_delete= models.CASCADE)
    products = JSONField(blank=True, default=list)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE,default=1,blank=True, null=True)
    status = models.IntegerField(choices=PAYMENT_STATUS, blank=True, null=True)
    delivered = models.BooleanField(default=False)
    total_price = models.CharField(max_length=255, blank=True)



    def __str__(self) -> str:
        return str(self.id)


    class Meta:
        db_table = "payment_model"
        