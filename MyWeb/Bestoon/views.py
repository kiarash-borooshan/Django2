# from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from json import JSONEncoder
# from Bestoon.models import User, Token, Expense, Income
# import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def welc(request):
    return HttpResponse("خوش آمدید")


@csrf_exempt
def submit_expense(request):
    print("submit_expense is OK")
    print(request.POST)

    # TODO: Validate data, user might be fake, amount might be fake

    # this_token = request.POST.get("token", "1234567")
    # this_token = 1234567
    # this_user = User.objects.filter(User, token__token=this_token).get()
    # now = datetime.datetime.now()
    # Expense.objects.create(User=this_user, Amount=request.POST['Amount'],
    #                        Text=request.POST["text"], Date=now)

    # print(this_token)
    # print(this_user)
    print("NEXT")

    return JsonResponse({
        "status": "ok"
    }, encoder=JSONEncoder)
