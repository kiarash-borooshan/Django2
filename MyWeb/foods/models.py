from django.db import models

# Create your models here.


class food(models.Model):
    Name = models.CharField(max_length=100,
                            verbose_name="نام غذا")
    Description = models.CharField(max_length=50,
                                   verbose_name="توضیحات")
    Rate = models.IntegerField(verbose_name="امتیاز",
                               default="0")
    Price = models.BigIntegerField(verbose_name="قیمت")
    Time = models.IntegerField(verbose_name="زمان لازم")
    Pub_date = models.DateTimeField(auto_now=False,
                                    auto_now_add=True,
                                    verbose_name="تاریخ")
    Photo = models.ImageField(upload_to="foods/image/",
                              verbose_name="تصویر")
    objects = models.Manager()

    def __str__(self):
        return self.Name
