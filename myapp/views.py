from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse


def view_history_temperature_list(request):
    resultList = Temperature_db.objects.all().order_by('-timestamp')
    for data in resultList:
        print(model_to_dict(data))

    # return HttpResponse("Viewiing history of tem.")
    return render(request, 'view_history_temperature.html', {'resultList': resultList, 'active': 'history'})

# from django.views.decorators.csrf import csrf_exempt 移到上面去了
@csrf_exempt
def add_temperature_API(request):
    try:
        if request.method == 'GET':
            sensor_id = request.GET ['sensor_id']
            temperature = request.GET['temperature']
            humidity = request.GET['humidity']
            print("GET")
            print(f"sensor_id:{sensor_id}, temperature:{temperature}, humidity:{humidity}")
        elif request.method == "POST":
            sensor_id = request.POST['sensor_id']
            temperature = request.POST['temperature']
            humidity = request.POST['humidity']
            print("POST")
            print(f"sensor_id : {sensor_id},temperature: {temperature},humidity: {humidity}")
        Temperature_db.objects.create(sensor_id=sensor_id, temperature=temperature, humidity=humidity)  
        return JsonResponse({"status": "success"})
    except :
        return JsonResponse({"status": "error"})
    # return HttpResponse("Adding temperature via API.")  

def add_temperature(request):
    if request.method == 'POST':
        sensor_id = request.POST['sensor_id']
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        Temperature_db.objects.create(sensor_id=sensor_id, temperature=temperature, humidity=humidity)
        #return HttpResponse("已送出資料")
        return redirect('view_history_temperature')
    
    else:        
        #return HttpResponse(request, "Adding temperature via web form.")
        return render(request, 'add_temperature.html', {'active': 'add'})

def show_temperature1(request):
    resultList=Temperature_db.objects.all().order_by('-timestamp')[:1]
    print(model_to_dict(resultList[0]))
    data = model_to_dict(resultList[0])
    return render(request, 'show _temperature1.html', {'data': data, 'active': 'show1'})

def show_temperature_API(request):
    resultList =Temperature_db.objects.all().order_by('-timestamp')[:1]
    resultList =list(resultList.values())
    #return JsonResponse({"message": "test"})
    return JsonResponse(resultList, safe=False) 

def show_temperature2(request):
  
    return render(request, 'show_temperature2.html', {'active': 'show2'})

