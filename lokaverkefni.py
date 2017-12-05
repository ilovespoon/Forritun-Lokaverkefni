import time
import random
import sys
# Andri Snær Didriksen
# 08.19.17

# Dæmi 1 def
def giska(tala,tala2):
    print(tala)
    try:
        if tala > tala2:
            #ef talan sem kom random er hærri þá er talan sem ég sló inn lægri
            print("of lágt, reyndu aftur... ")
            return True
        elif tala2 > tala:
            # Ef talan sem ég sló inn er hærri þá kemur að random sé lægri
            print("of hátt, reyndu aftur... ")
            return True
        # ef það kemur match þá vinn ég
        elif tala == tala2:
            print("Til hamingju, þú fannst töluna... ")
            return False
    except ValueError:
        print("Vitlaust... ")
# Dæmi 2 def
def kasta_pening(teljari,teljari2,):
    print("skjaldmerki: ",str(teljari),"Loðna: ",str(teljari2))

teljari = 0
telajri2 = 0




flag=True
while flag==True:
#Valmynd
    print("--------Valmynd--------")
    print("Liður 1: ") # virkar en í raunini en breytist alltaf þegar ég giska á töluna
    print("Liður 2: ")
    print("Liður 3: ")
    print("Hætta 4: ")

    val=input("Sláðu inn lið... ")

    if val == "1":
        while True:
            try:
                print("Dæmi 1")
                #þarf að slá inn tölu milli 1-1000
                tala = random.randint(1,1000)
                tala2 = int(input("Sláðu inn tölu á milli 1 og 1000... "))
                giska(tala,tala2)
            except:
                print("Þú hefur ekki slegið inn tölu... ")

    if val == "2":
        while True:
            print("1. Kasta pening: ")
            print("2. Hætta")
            tala = int(input("Hvað villtu gera: "))
            tala2 = random.randint(1,2)
            if tala == 1:
                teljari +=1
            elif tala2 == 2:
                teljari2 +=1
    else:
        print("Vitlaust... ")
        True
    kasta_pening(teljari,teljari2)
