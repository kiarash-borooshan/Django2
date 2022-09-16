"""MyWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Bestoon import views as BestoonView
from foods import views as FoodView

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("welcome/", BestoonView.welc, name="welcome"),
    path("submit/expense/", BestoonView.submit_expense),
    # path("welcome/", include("Bestoon.url"))
    path("foods/", FoodView.food_welc),
    path("food list/", FoodView.food_list),
    path("food list/<int:food_id>/", FoodView.food_details, name="detail"),
    path("food article/", FoodView.food_article, name="food_article")
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
