from django.shortcuts import render
from django.http import HttpResponse
from .models import food


# Create your views here.

def food_welc(request):
    return HttpResponse("به صفحه غذا خوش آمدید ")


def food_list(request):
    cont = {
        "foods": food.objects.all()
    }

    return render(request,
                  template_name="foodList.html",
                  context=cont)
