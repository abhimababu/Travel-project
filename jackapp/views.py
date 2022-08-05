from django.shortcuts import render
from .models import drink


# from django.shortcuts import HttpResponse
# Create your views here.


def fun(request):
    obj = drink.objects.all()
    # obj=drink()
    # obj.name="Soft Wine"
    # obj.desc="This is good for health"
    return render(request, 'index.html', {'result': obj})


# return render(request, 'form.html')


# def addition(request):
# num1 = int(request.POST["num1"])
# num2 = int(request.POST["num2"])
# num3 = num1 + num2
# return render(request, "result.html", {"add": num3})
