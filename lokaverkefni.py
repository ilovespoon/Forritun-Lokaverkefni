#Andri Snær Didriksen Ásmundsson og Skúli Guðbrandsson
# 24.11.2917
from json import*
from random import*



listi = []

def bill__init__(self):
    bill








def vidskiptavinur(self):
    d=[{"Nafn": "konni", "Heimilisfang": "Hraunbraut 27","Kennitala":"2712576789","Þjóðerni":"ísl"},
        {"Nafn": "sonni", "Heimilisfang": "Launbraut 27","Kennitala":"2812576789","Þjóðerni":"dan"}
        ]
    #skrifa inn í json skrá
    with open("konni.json", "w",encoding='utf-8') as json_file:
        json_file.write(json.dumps(d))

    #lesa skrá
    with open("konni.json", "r",encoding='utf-8') as json_file:
        listi = json.loads(json_file.read())
    for dic in listi:
        for k,v in dic.items():
            print(k," => ",v)
    # setja inn nýja færslu
    x={}
    x["Nafn"]=input("Sláðu inn Nafn ")
    x["Heimilisfang"]=input("Sláðu inn heimili ")
    x["Kennitala"]=input("Sláðu inn kennitölu ")
    x["Þjóðerni"]=input("Sláðu inn þjóðerni ")
    d.append(x)
    with open("konni.json", "w") as json_file:
        json_file.write(json.dumps(d))
    with open("konni.json", "r") as json_file:
        listi = json.loads(json_file.read())
    print("------------------Viðskiptavinir---------------------")
    for dic in listi:
        for k,v in dic.items():
            print(k," => ",v)
        print("---------------------------------------------")
