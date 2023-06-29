from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.

class RestaurantInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    상호명 = models.CharField(max_length=50)
    상권업종중분류명 = models.CharField(max_length=50)
    도로명주소 = models.CharField(max_length=50)
    경도 = models.FloatField()
    위도 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'restaurant_info'

    # def __str__(self):
    #     return self.상호명
class AllUsersOrderList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    상권업종중분류명 = models.CharField(max_length=50, null=False)
    상호명 = models.CharField(max_length=20, null=False)

    class Meta:
        managed = True

class AllUsersOrderCount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    닭오리요리 = models.IntegerField(null=False, default=0)
    별식퓨전요리 = models.IntegerField(null=False, default=0)
    부페 = models.IntegerField(null=False, default=0)
    분식 = models.IntegerField(null=False, default=0)
    양식 = models.IntegerField(null=False, default=0)
    일식수산물 = models.IntegerField(null=False, default=0)
    제과제빵떡케익 = models.IntegerField(null=False, default=0)
    중식 = models.IntegerField(null=False, default=0)
    커피점카페 = models.IntegerField(null=False, default=0)
    패스트푸드 = models.IntegerField(null=False, default=0)
    한식 = models.IntegerField(null=False, default=0)

    class Meta:
        managed = True


class UsersAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)