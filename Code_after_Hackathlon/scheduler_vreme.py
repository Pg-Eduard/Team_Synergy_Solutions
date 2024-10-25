from vreme import get_vreme
from datetime import datetime as time
import pandas as pd
import mUsi as mu
import ventilator as vent
import mIncalzire as mi
import mLumini_ext as mlx

current_time = time.now()
hour = int(current_time.strftime("%H"))
status_vreme = get_vreme()

def day_time(): #actiune in functie de timp
    stare_lumini = pd.read_excel("static/ext.xlsx")
    if hour >= 8 and hour <= 20:
        print("True, zi")
        if stare_lumini["Status"][0] == 0:
            mlx.stareLumini_ext() #se sting luminile ext
    if hour > 20 or hour < 8:
        print("True, noapte")
        if stare_lumini["Status"][0] == 1:
            mlx.stareLumini_ext() #se aprind luminile ext

def vreme(): #actiune in functie de vreme
    humidity = int(float(status_vreme["humidity"]))
    caldura = int(float(status_vreme["feelslike"]))
    stare_usa = open("/home/eduardPi/Desktop/Programe licenta/Usi/garaj.txt").read()
    stare_ventilator = pd.read_excel("static/vent.xlsx")
    stare_ventilator = stare_ventilator["State"][0]
    stare_incalzire = pd.read_excel("static/incalzire.xlsx")
    print(stare_ventilator)

    if humidity >= 80:
        print("Vreme ploioasa")
        if stare_usa == 1:
            mu.usaGaraj() #inchide usa
        if stare_ventilator == 1:
            vent.selectState() #opreste ventilatorul
    else:
        print("Vreme insorita")
        if stare_usa == 0:
            mu.usaGaraj() #deschide usa
        if stare_ventilator == 0:
            vent.selectState() #porneste ventilatorul
    if caldura > 24:
        print("Vreme calduroasa")
        if stare_ventilator == 1:
            vent.selectState() #porneste ventilatorul
        if stare_incalzire["Status"][0] == 1:
            mi.stareIncazlire() #opreste caldura
    else:
        print("Vreme friguroasa")
        if stare_ventilator == 0:
            vent.selectState() #opreste ventilatorul
        if stare_incalzire["Status"][0] == 0:
            mi.stareIncazlire() #porneste caldura