# Iseseisev töö 02
# Erki Rehkli
# 04.02.21
import math
import random
from random import randrange

#2.5 Õunad

ppõun=0
õun=0

pp = int(input("Mitu pöialpoissi tahab õunu? :"))
for i in range(pp):
    ppõun = random.randrange(1,3)
    õun = õun + ppõun
    print(ppõun)
lvõun= 14 - õun
print("Lumivalgeksele jäi:",lvõun,"õuna")
    
##############################

#2.4 Täringud

arv = 0

t = int(input("Täringute arv :"))
for x in range(t):
    print(randrange(1,6))
    arv += 1

##############################

#2.3 Murelikud lapsevanemad

ringid = int(input("Sisesta ringide arv :"))

arv = 0

porgandid = 0

while(arv < ringid):
    arv += 1
    if (arv % 2) == 0:
        porgandid += arv
print("Porgandite koguarv:" +str(porgandid))

##############################

#2.2 Äratus

kordus = int(input("Sisesta mitu korda äratada :"))
for i in range(0,kordus):
    print("Tõuse ja sära")

##############################

#2.1 Bussid

inimarv = int(input("Inimeste arv :"))
kohtadearv = int(input("Kohtade arv :"))
bussidearv =math.ceil(inimarv / kohtadearv)
print("Busse vaja:",bussidearv)
viimanebuss = inimarv % kohtadearv
if viimanebuss > 0:
    print("Viimases bussis inimesi:",viimanebuss)
else:
    print("Viimases bussis inimesi: 40")



    

