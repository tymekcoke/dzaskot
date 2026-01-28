import modul_wlasny_nrAlbumu as modul

print("TEST 1: miejsca_zerowe_kwadratowa")
print()

# Test 1
wynik = modul.miejsca_zerowe_kwadratowa(1, -5, 6)
if wynik == (2.0, 3.0):
    print("Test 1.1 OK - wynik:", wynik)
else:
    print("Test 1.1 BLAD - wynik:", wynik)

# Test 2
wynik = modul.miejsca_zerowe_kwadratowa(1, -4, 4)
if wynik == (2.0, 2.0):
    print("Test 1.2 OK - wynik:", wynik)
else:
    print("Test 1.2 BLAD - wynik:", wynik)

# Test 3
wynik = modul.miejsca_zerowe_kwadratowa(1, 0, 1)
if wynik == "Brak miejsc zerowych":
    print("Test 1.3 OK - wynik:", wynik)
else:
    print("Test 1.3 BLAD - wynik:", wynik)

# Test 4
wynik = modul.miejsca_zerowe_kwadratowa(0, 2, 1)
if "Blad" in wynik:
    print("Test 1.4 OK - wynik:", wynik)
else:
    print("Test 1.4 BLAD - wynik:", wynik)

print()
print("TEST 2: oblicz_sinus_stopnie")
print()

# Test 1
wynik = modul.oblicz_sinus_stopnie(0)
if wynik == 0.0:
    print("Test 2.1 OK - sin(0) =", wynik)
else:
    print("Test 2.1 BLAD - sin(0) =", wynik)

# Test 2
wynik = modul.oblicz_sinus_stopnie(90)
if wynik == 1.0:
    print("Test 2.2 OK - sin(90) =", wynik)
else:
    print("Test 2.2 BLAD - sin(90) =", wynik)

# Test 3
wynik = modul.oblicz_sinus_stopnie(30)
if abs(wynik - 0.5) < 0.001:
    print("Test 2.3 OK - sin(30) =", wynik)
else:
    print("Test 2.3 BLAD - sin(30) =", wynik)

# Test 4
wynik = modul.oblicz_sinus_stopnie("tekst")
if wynik == 0.0:
    print("Test 2.4 OK - zastapiono zla wartosc na 0")
else:
    print("Test 2.4 BLAD")

print()
print("TEST 3: oblicz_cosinus_z_tangensem")
print()

# Test 1
wynik = modul.oblicz_cosinus_z_tangensem(0)
if abs(wynik - 1.0) < 0.001:
    print("Test 3.1 OK - cos(0) =", wynik)
else:
    print("Test 3.1 BLAD - cos(0) =", wynik)

# Test 2
wynik = modul.oblicz_cosinus_z_tangensem(60)
if abs(wynik - 0.5) < 0.001:
    print("Test 3.2 OK - cos(60) =", wynik)
else:
    print("Test 3.2 BLAD - cos(60) =", wynik)

# Test 3
wynik = modul.oblicz_cosinus_z_tangensem(45)
if abs(wynik - 0.707107) < 0.001:
    print("Test 3.3 OK - cos(45) =", wynik)
else:
    print("Test 3.3 BLAD - cos(45) =", wynik)

# Test 4
wynik = modul.oblicz_cosinus_z_tangensem(90)
if abs(wynik - 0.707107) < 0.001:
    print("Test 3.4 OK - zastapiono 90 stopni na 45 stopni")
else:
    print("Test 3.4 BLAD")

print()
print("TEST 4: oblicz_srednia_geometryczna")
print()

# Test 1
wynik = modul.oblicz_srednia_geometryczna([1, 2, 3])
if abs(wynik - 1.817121) < 0.001:
    print("Test 4.1 OK - srednia [1,2,3] =", wynik)
else:
    print("Test 4.1 BLAD - srednia [1,2,3] =", wynik)

# Test 2
wynik = modul.oblicz_srednia_geometryczna([4, 9])
if wynik == 6.0:
    print("Test 4.2 OK - srednia [4,9] =", wynik)
else:
    print("Test 4.2 BLAD - srednia [4,9] =", wynik)

# Test 3
wynik = modul.oblicz_srednia_geometryczna([])
if "Blad" in wynik:
    print("Test 4.3 OK - blad dla pustej listy")
else:
    print("Test 4.3 BLAD")

print()
print("TEST 5: oblicz_odchylenie_standardowe")
print()

# Test 1
wynik = modul.oblicz_odchylenie_standardowe([1, 2, 3, 4, 5])
if abs(wynik - 1.414214) < 0.001:
    print("Test 5.1 OK - odchylenie [1,2,3,4,5] =", wynik)
else:
    print("Test 5.1 BLAD - odchylenie [1,2,3,4,5] =", wynik)

# Test 2
wynik = modul.oblicz_odchylenie_standardowe([10, 10, 10])
if wynik == 0.0:
    print("Test 5.2 OK - odchylenie [10,10,10] =", wynik)
else:
    print("Test 5.2 BLAD - odchylenie [10,10,10] =", wynik)

# Test 3
wynik = modul.oblicz_odchylenie_standardowe([5])
if "Blad" in wynik:
    print("Test 5.3 OK - blad dla 1 elementu")
else:
    print("Test 5.3 BLAD")

print()
print("Koniec testow")
