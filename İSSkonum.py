# -*- coding: utf-8 -*-
import requests

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("EĞER İSS İN ANLIK KONUMUNU GÖRMEK İSTİYORSANIZ ENTER A TIKLAYIN")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
yanıt = input()

turkey_longitudes = []
turkey_latitudes = []

#25.9090 to 44.5742
#i = 25.9090
#a = 44.5742
i = 95.1212
a = 135.1212
while i < a :
    turkey_longitudes.append("{:10.4f}".format(i))
    i += 0.0001

#35.9025 to 42.02683
#j = 35.9025
#b = 42.0268
j = 15.1212
b = 40.1212
while j < b :
    turkey_latitudes.append("{:10.4f}".format(j))
    j += 0.0001
if yanıt == "":
    while 1>0:
        ISScevap = requests.get("http://api.open-notify.org/iss-now.json")
        ISSkonum = ISScevap.json()["iss_position"]
        ISSlatitude = ISScevap.json()["iss_position"]["latitude"]
        ISSlongitude = ISScevap.json()["iss_position"]["longitude"]
        print(ISSkonum)
        for coordinate_longitudes in turkey_longitudes:
            if ISSlongitude == 33.2222:
                print("long: ",coordinate_longitudes)
                for coordinate_latitudes in turkey_latitudes:
                    print("lat: ",coordinate_latitudes)
                    if ISSlatitude == coordinate_latitudes:
                        print("YOK ARTIK İSS ŞUAN TÜRKİYENİN ÜSTÜNDE")
                        

            
       
