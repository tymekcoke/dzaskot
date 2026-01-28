import modul_wlasny_nrAlbumu as modul

def test_miejsca_zerowe():
    print("TEST 1: miejsca_zerowe_kwadratowa")

    wynik = modul.miejsca_zerowe_kwadratowa(1, -5, 6)
    assert wynik == (2.0, 3.0), "Test 1.1 nie przeszedl"
    print("Test 1.1 OK")

    wynik = modul.miejsca_zerowe_kwadratowa(1, -4, 4)
    assert wynik == (2.0, 2.0), "Test 1.2 nie przeszedl"
    print("Test 1.2 OK")

    wynik = modul.miejsca_zerowe_kwadratowa(1, 0, 1)
    assert wynik == "Brak miejsc zerowych", "Test 1.3 nie przeszedl"
    print("Test 1.3 OK")

    wynik = modul.miejsca_zerowe_kwadratowa(0, 2, 1)
    assert "Blad" in wynik, "Test 1.4 nie przeszedl"
    print("Test 1.4 OK")
    print()

def test_sinus():
    print("TEST 2: oblicz_sinus_stopnie")

    wynik = modul.oblicz_sinus_stopnie(0)
    assert wynik == 0.0, "Test 2.1 nie przeszedl"
    print("Test 2.1 OK")

    wynik = modul.oblicz_sinus_stopnie(90)
    assert wynik == 1.0, "Test 2.2 nie przeszedl"
    print("Test 2.2 OK")

    wynik = modul.oblicz_sinus_stopnie(30)
    assert abs(wynik - 0.5) < 0.001, "Test 2.3 nie przeszedl"
    print("Test 2.3 OK")

    wynik = modul.oblicz_sinus_stopnie(180)
    assert abs(wynik) < 0.000001, "Test 2.4 nie przeszedl"
    print("Test 2.4 OK")

    wynik = modul.oblicz_sinus_stopnie("tekst")
    assert wynik == 0.0, "Test 2.5 nie przeszedl"
    print("Test 2.5 OK")
    print()

def test_cosinus():
    print("TEST 3: oblicz_cosinus_z_tangensem")

    wynik = modul.oblicz_cosinus_z_tangensem(0)
    assert abs(wynik - 1.0) < 0.001, "Test 3.1 nie przeszedl"
    print("Test 3.1 OK")

    wynik = modul.oblicz_cosinus_z_tangensem(60)
    assert abs(wynik - 0.5) < 0.001, "Test 3.2 nie przeszedl"
    print("Test 3.2 OK")

    wynik = modul.oblicz_cosinus_z_tangensem(45)
    assert abs(wynik - 0.707107) < 0.001, "Test 3.3 nie przeszedl"
    print("Test 3.3 OK")

    wynik = modul.oblicz_cosinus_z_tangensem(90)
    assert abs(wynik - 0.707107) < 0.001, "Test 3.4 nie przeszedl"
    print("Test 3.4 OK")

    wynik = modul.oblicz_cosinus_z_tangensem([1, 2])
    assert wynik == 1.0, "Test 3.5 nie przeszedl"
    print("Test 3.5 OK")
    print()

def test_srednia():
    print("TEST 4: oblicz_srednia_geometryczna")

    wynik = modul.oblicz_srednia_geometryczna([1, 2, 3])
    assert abs(wynik - 1.817121) < 0.001, "Test 4.1 nie przeszedl"
    print("Test 4.1 OK")

    wynik = modul.oblicz_srednia_geometryczna([4, 9])
    assert wynik == 6.0, "Test 4.2 nie przeszedl"
    print("Test 4.2 OK")

    wynik = modul.oblicz_srednia_geometryczna([])
    assert "Blad" in wynik, "Test 4.3 nie przeszedl"
    print("Test 4.3 OK")

    wynik = modul.oblicz_srednia_geometryczna([1, -2, 3])
    assert "Blad" in wynik, "Test 4.4 nie przeszedl"
    print("Test 4.4 OK")
    print()

def test_odchylenie():
    print("TEST 5: oblicz_odchylenie_standardowe")

    wynik = modul.oblicz_odchylenie_standardowe([1, 2, 3, 4, 5])
    assert abs(wynik - 1.414214) < 0.001, "Test 5.1 nie przeszedl"
    print("Test 5.1 OK")

    wynik = modul.oblicz_odchylenie_standardowe([10, 10, 10])
    assert wynik == 0.0, "Test 5.2 nie przeszedl"
    print("Test 5.2 OK")

    wynik = modul.oblicz_odchylenie_standardowe([5])
    assert "Blad" in wynik, "Test 5.3 nie przeszedl"
    print("Test 5.3 OK")

    wynik = modul.oblicz_odchylenie_standardowe("tekst")
    assert "Blad" in wynik, "Test 5.4 nie przeszedl"
    print("Test 5.4 OK")
    print()

# Uruchomienie testow
test_miejsca_zerowe()
test_sinus()
test_cosinus()
test_srednia()
test_odchylenie()

print("Wszystkie testy przeszly!")
