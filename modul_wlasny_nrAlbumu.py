import numpy as np
import math
from scipy import stats

# znajduje miejsca zerowe funkcji kwadratowej
def miejsca_zerowe_kwadratowa(a, b, c):
    if a == 0:
        return "Blad: a nie moze byc 0"

    delta = b**2 - 4*a*c

    if delta < 0:
        return "Brak miejsc zerowych"
    elif delta == 0:
        x = -b / (2*a)
        return (x, x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return (x1, x2)


# liczy sinus kata w stopniach
def oblicz_sinus_stopnie(kat):
    if not isinstance(kat, (int, float)):
        print("Blad: kat musi byc liczba, uzyto 0 stopni")
        kat = 0

    kat_rad = math.radians(kat)
    wynik = math.sin(kat_rad)
    return round(wynik, 6)


# liczy cosinus przez tangens
def oblicz_cosinus_z_tangensem(kat):
    if not isinstance(kat, (int, float)):
        print("Blad: kat musi byc liczba, uzyto 0 stopni")
        kat = 0

    if kat % 90 == 0 and kat % 180 != 0:
        print("Blad: tangens nieokreslony, uzyto 45 stopni")
        kat = 45

    kat_rad = math.radians(kat)
    tangens = math.tan(kat_rad)
    cosinus = 1 / math.sqrt(1 + tangens**2)

    if kat > 90 and kat < 270:
        cosinus = -abs(cosinus)

    return round(cosinus, 6)


# liczy srednia geometryczna
def oblicz_srednia_geometryczna(liczby):
    if not isinstance(liczby, (list, tuple)):
        return "Blad: to musi byc lista"

    if len(liczby) == 0:
        return "Blad: lista pusta"

    if any(x <= 0 for x in liczby):
        return "Blad: liczby musza byc dodatnie"

    wynik = stats.gmean(liczby)
    return round(wynik, 6)


# liczy odchylenie standardowe
def oblicz_odchylenie_standardowe(liczby):
    if not isinstance(liczby, (list, tuple)):
        return "Blad: to musi byc lista"

    if len(liczby) < 2:
        return "Blad: potrzeba min 2 liczby"

    wynik = np.std(liczby)
    return round(wynik, 6)
