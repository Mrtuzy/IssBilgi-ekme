# -*- coding: utf-8 -*-
import requests
import json

cevap = requests.get("http://api.open-notify.org/astros.json")

uzaydaki_kişiSayısı = cevap.json()["number"]
print(cevap)
print("ŞUAN UZAYDA "+str(uzaydaki_kişiSayısı)+" KİŞİ VAR")
print("___________________")
for x in range(0,uzaydaki_kişiSayısı):
    print("Adı: "+cevap.json()["people"][x]["name"])
    print("Bulunduğu İstasyon: "+cevap.json()["people"][x]["craft"])
    print("-------")





