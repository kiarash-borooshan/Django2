from django.shortcuts import render
from django.http import HttpResponse
from .models import food
# from django.shortcuts import get_object_or_404


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


def food_details(request, food_id):
    contxt = {
        "food": food.objects.get(id=food_id)
    }
    return render(request,
                  template_name="food_details.html",
                  context=contxt)
