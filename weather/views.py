from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=d4492d47cbe127cd78a156f0a281eb28').read()  #result of request from url
        json_data=json.loads(res)
        data = {
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        city=""
        data={}
    return render(request,'index.html',{'city':city,'data':data})
