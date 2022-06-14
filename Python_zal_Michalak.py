from tkinter import *
okno = Tk()
okno.title("Wszechstronny kalkulator") 
okno.geometry('350x150')


def cofnij():
    okno_waga.grid_forget()
    okno_wynik.grid_forget()
    okno_wzrost.grid_forget()
    wzrost.grid_forget() 
    waga.grid_forget()
    przycisk_obliczbmi.grid_forget()
    kalkulator_bmi.place(x = 125, y = 30)
    przycisk_cofnij.grid_forget()
    wynik.place_forget()
    efekt_bmi.place_forget()
    kalkulator_wyn.place(x = 100, y = 70)
    napis_wynbrutto.grid_forget()
    napis_rodzaj_umowy.grid_forget()
    rad_oprace.grid_forget()
    rad_zlecenie.grid_forget()
    okno_wynbrutto.grid_forget()
    napis_wynik.grid_forget()
    przycisk_obliczwyn.grid_forget()
    przycisk_cofnij.grid_forget()
    wynik_wysw.grid_forget()
    okno_wynbrutto.grid_forget()
    
    
## Kalkulator BMI    
  
def def_kalk_bmi():
    okno_waga.grid(column = 0, row = 1)
    okno_wynik.grid(column = 0, row = 2)
    okno_wzrost.grid(column = 0, row = 0)
    wzrost.grid(column = 1, row = 0) 
    waga.grid(column = 1, row = 1)
    przycisk_obliczbmi.grid(column = 3, row = 1)
    kalkulator_bmi.place_forget()
    przycisk_cofnij.grid(column = 3, row = 0)
    kalkulator_wyn.place_forget()
    napis_wynbrutto.grid_forget()
    napis_rodzaj_umowy.grid_forget()
    rad_oprace.grid_forget()
    rad_zlecenie.grid_forget()
    okno_wynbrutto.grid_forget()
    napis_wynik.grid_forget()
    przycisk_obliczwyn.grid_forget()
    
kalkulator_bmi = Button(okno, text = "Kalkulator BMI", command = def_kalk_bmi)
kalkulator_bmi.place(x = 125, y = 30)

wzrost_zmienna = DoubleVar()
waga_zmienna = DoubleVar()
okno_wzrost = Label(okno, text = "Wpisz swój wzrost (m):")
wzrost = Entry(okno, width = 8, textvariable = wzrost_zmienna)
okno_waga = Label(okno, text = "Wpisz swoją wagę (kg):")
waga = Entry(okno, width = 8, textvariable = waga_zmienna)
okno_wynik = Label(okno, text = "Oto twój wynik:")

def obliczanie_bmi():
    global bmi
    bmi1 = waga_zmienna.get()
    bmi2 = wzrost_zmienna.get()
    bmi = bmi1 / (bmi2 * bmi2)
    global wynik
    wynik.config(text = str(bmi))
    wynik.place(x = 110, y = 52)
    
    if bmi < 18.5:
        odp = "Musisz więcej wsuwać..."
    elif bmi >= 18.5 and bmi < 24.9:
        odp = "Wspaniale się odżywiasz!"
    elif bmi >= 24.9 and bmi < 33:
        odp = "Chyba musisz schudnąć..."
    else: 
        odp = "Ojjj ty grubasku mały... ;)"
    efekt_bmi.config(text = str(odp))
    efekt_bmi.place(x = 75, y = 90)
    
bmi = 0
wynik = Label(okno)
odp = 0
efekt_bmi = Label(okno, font = ("Times New Roman", 16), relief = SUNKEN)
    
przycisk_obliczbmi = Button(okno, text = "Oblicz BMI", command = obliczanie_bmi)
przycisk_cofnij = Button(okno, text = "Cofnij", command = cofnij)



## Kalkulator wynagrodzenia netto

def def_kalk_wynagr():
    kalkulator_bmi.place_forget()
    kalkulator_wyn.place_forget()
    napis_wynbrutto.grid(column = 0, row = 0)
    napis_rodzaj_umowy.grid(column = 0, row = 1)
    rad_oprace.grid(column = 0, row = 2)
    rad_zlecenie.grid(column = 1, row = 2)
    okno_wynbrutto.grid(column = 1, row = 0)
    napis_wynik.grid(column = 0, row = 5)
    przycisk_obliczwyn.grid(column = 3, row = 1)
    przycisk_cofnij.grid(column = 3, row = 0)


wyn_brutto = DoubleVar()
napis_wynbrutto = Label(okno, text = "Wynagrodzenie brutto:")
napis_rodzaj_umowy = Label(okno, text = "Podaj rodzaj zatrudnienia:")
okno_wynbrutto = Entry(okno, width = 8, textvariable = wyn_brutto)
napis_wynik = Label(okno, text = "Oto Twoje zarobki netto:")
wartosc = IntVar()
rad_oprace = Radiobutton(okno, text = "Umowa o pracę", variable = wartosc, value = 1,
                         command = lambda: obl_wynagrodzenia())
rad_zlecenie = Radiobutton(okno, text = "Umowa zlecenie", variable = wartosc, value = 2,
                           command = lambda: obl_wynagrodzenia())

zmienna = StringVar()
wynik_wysw = Label(okno, textvariable = zmienna)

def obl_wynagrodzenia():
    brutto = wyn_brutto.get()
    global wyn_netto
    if wartosc.get() == 1:
       wyn_netto = round((brutto * 72.98) / 100, 2)
    elif wartosc.get() == 2:
       wyn_netto = round((brutto * 85.16) / 100, 2)
       wyn_netto = str(wyn_netto)
    zmienna.set(wyn_netto)
    wynik_wysw.grid(column = 1, row = 5)

przycisk_obliczwyn = Button(okno, text = "Oblicz", command = obl_wynagrodzenia)
przycisk_cofnij = Button(okno, text = "Cofnij", command = cofnij)
kalkulator_wyn = Button(okno, text = "Kalkulator wynagrodzeń", command = def_kalk_wynagr)
kalkulator_wyn.place(x = 100, y = 70)


okno.mainloop()