# Andri Snær Didriksen Ásmundsson og Skúli Guðbrandsson
# 24.11.2917

from json import*
from random import*

#Klasssi fyrir viðskifta vininn
class Vidskiptavinur:
    def __init__(self,nafn,heimili,kt,þjoderni,okt,simi,postur):
        self.nafn = nafn
        self.hemili = heimili
        self.kt =kt
        self.þjoderni = þjoderni
        self.okt = okt
        self.simi = simi
        self.postur = postur
    # þetta fall les texta skrá sem heldur um uplísingar um vidskiftavinn og prentar það svo út
    def readVIdskiftavindur(self):
        vidskipavinur = []

        with open("vidskiftavinur.txt", "r") as bill1:
            lina = bill1.read().splitlines()

            for x in lina:
                vidskipavinur.append(x.split(","))

        for madur in vidskipavinur:
            for x in madur:
                print(x,end="  ")
            print()


class bill:
    # þetta er klasssi fyrir bílana
    def __init__(self,skranr,argerd,tegund,framledari,ath,leyfilegurfjoldimanna):
        self.skranr = skranr
        self.argerd = argerd
        self.tegund = tegund
        self.framledari = framledari
        self.ath = ath
        self.leyfilegurfjoldimanna = leyfilegurfjoldimanna
    # þetta fall les texta skrá sem heldur um uplísingar um bíla og prenta það svo út
    def readFile(self):
        val = input("hvernig bíl ertu að leita af jeppi sportsbill eða folksbill")

        bilar = []
        lina = ""
        with open("bill.txt", "r") as bill1:
            lina = bill1.read()
            bilar = lina.split(":")
            bilar.remove("")
        print(bilar)
        temp = []
        for x in bilar:
            temp = x.split(",")

            print(val)
            temp[2] = temp[2][1:-1]
            #print("verður svona", temp[2])
            if val == temp[2]:
                print(temp)


# Klassi fyrir pantanir
class pantanair:
    def __init__(self,audkenni,vidskiptavinir,pontunardagur,ath):
        self.audkenni = audkenni
        self.vidskiptavinir = vidskiptavinir
        self.pontunardagur = pontunardagur
        self.ath = ath
    # þetta fall les texta skrár sem heldur um pantanir á bílum og prenta svo það út
    def readpantanair(self):
        pantanir = []
        lina = ""

        with open("pontun.txt", "r") as pontun1:
            lina = pontun1.read().splitlines()
            for x in lina:
                pantanir.append(x.split(","))
        for x in pantanir:
            print(x)
            print(x[0])

# Klassi fyrir bilaleigu
class bilalegia:
    # þetta fall les texta skrá sem heldur um uplýsingar um bílaleigu fyrir bíla
    def readbilalega(self,val,val2):
        listi = []
        val = input("hvaða bíl ertu að leita af")
        val2 = input("hvaða viku vilt þú leigja")
        listi.append(val+":"+val2)

        flag=False
        with open("bilaleiga.txt","r") as bilalegan:
            linur = bilalegan.read().splitlines()
            print(linur)
            print(listi)
            for x in linur:
                temp=x.split(":")
                print(val2,temp[1])
                if temp[0]==val and val2 != temp[1]:
                    print("þú valdir að leigja bílinn :",val,"og í viku :",val2)
                    flag=True
                    break
        with open("bilaleiga.txt","a") as bilalegan:
            bilalegan.write(val+":"+val2+"\n")
        with open("bilaleiga.txt","r") as bilalegan:
            read = bilalegan.read()
            print(read)


            if flag==False:
                    print("Bíll ekki til...")


svar = " "
while svar == " ":
    print("1 = Prenta út Vidskiptavinur: ")
    print("2 = Prenta út Bíll: ")
    print("3 = Prenta út Pantanair: ")
    print("4 = Prenta út Bílaleiga: ")
    print("5 = Hætta í Forriti: ")
    val = int(input("hvað vilt þú velja?: "))

    if val == 1:
        print("Þú hefur valið að Prenta út Vidskiptavini. ")
        print("----------------------------------------------")
        a = Vidskiptavinur("","","","","","","")
        print(a.readVIdskiftavindur())
        print("----------------------------------------------")

    if val == 2:
        print("Þú hefur valið að Prenta út Bíla. ")
        print("----------------------------------------------")
        b = bill("","","","","","")
        print(b.readFile())
        print("----------------------------------------------")


    if val == 3:
        print("Þú hefur valið að Prenta út Pantanair. ")
        print("----------------------------------------------")
        p = pantanair("","","","")
        print(p.readpantanair())
        print("----------------------------------------------")


    if val == 4:
        print("----------------------------------------------")
        print("Þú hefur valið að Prenta út Bílaleigu. ")
        bl = bilalegia()
        print(bl.readbilalega("",""))
        print("----------------------------------------------")


    if val == 5:
        svar = input("vilt þú hætta? Y/N ")