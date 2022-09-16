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


""" create food rticles """
def food_article(request):
    Contxt = {
        "articles": [
            {"title": "طرز تهیه آش انار",
             "thumbnail": "https://chishi.ir/wp-content/uploads/2020/12/ash-anar.jpg",
             "description": "های خوشمزه و سنتی ایرانی است که در شهرهای مختلف کشور با دستورهای بسیار متنوعی تهیه می شود. این آش خوشمزه در شهرهای مختلف کشور برای مناسبت های خاص تهیه می شود که یکی از مهم ترین این مناسبت ها، بلندترین شب سال یعنی شب یلدا می باشد که تقریبا تمام غذاها و دسرها با موادی مثل انار و کدو حلوایی تهیه می شوند. آش انار علاوه بر اینکه طعم بسیار خوبی دارد، دارای ظاهری شیک و مجلسی می باشد و به همین دلیل می توانیم آنرا در کاسه های کوچک برای پیش غذا یا عصرانه هم سرو کنیم، برای مشاهده این آموزش آشپزی در ادامه با سای"},
            {"title": "غذا با بادمجان",
             "thumbnail": "https://chishi.ir/wp-content/uploads/2021/05/ghaza-ba-bademjan.jpg",
             "description": "ف در آشپزی ایرانی است که با ان غذاهای بسیار متنوعی تهیه می شود. غذاهایی که با بادمجان تهیه می شوند، تقریبا تمام دسته بندی های غذایی مثل غذاهای فوری، غذاهای سنتی و غذاهای فست فودی را پوشش می دهند. البته شاید به طور معمول اگر از ما سوال کنند چند غذا با بادمجان نام ببرید، شاید نتوانیم خیلی از غذاهایی که با بادمجان تهیه می شوند را به خاطر آوریم، با بوکمارک کردن این صفحه می توانید یک فهرست کامل از غذاهایی که با بادمجان تهیه می شوند را به صورت آنلاین در هر نقطه ای در دسترس داشته"},
            {"title": "طرز تهیه خورش کرفس با لوبیا",
             "thumbnail": "https://chishi.ir/wp-content/uploads/2021/03/khoresh-karaf-loobia.jpg",
             "description": "ست که از ترکیب گوشت ، کرفس و لوبیا تهیه می شود. چاشنی های مورد استفاده در این خورش، رب گوجه و رب نارنج است. عطر و بوی سبزی و کرفس در خورش، طعم فوق العاده ای به غذا می دهد. این خورش بسیار خوشمزه را می توان با تکه های مرغ هم تهیه نمود. این خورش را با برنج زعفرانی یا کته س"},
        ]
    }
    return render(request=request,
                  template_name="food_article.html",
                  context=Contxt)