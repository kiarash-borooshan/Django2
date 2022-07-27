from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    Text = models.CharField(max_length=255,
                            verbose_name="توضیحات")
    Amount = models.BigIntegerField(verbose_name="هزینه")
    Date = models.DateTimeField(verbose_name="تاریخ")
    User = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name=None,
                             verbose_name="کاربر")
    Choice = (("lunch", "نهار"),
              ("dinner", "شام"))
    Choose = models.CharField(max_length=255,
                              choices=Choice,
                              default="lunch",
                              verbose_name="انتخاب کنید")

    def __str__(self):
        return f"تومان{self.Amount}  - {self.Date}"
