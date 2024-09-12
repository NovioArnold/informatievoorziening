import math

#getal1 = int(input("Geef een getal: "))
#getal2 = int(input("Geef nog een getal: "))

naam = input("Geef je naam: ")
wachtwoord = input("Geef je wachtwoord: ")
print(f'Hello {naam}, je wachtwoord is {wachtwoord}')

if naam == 'Jeroen' and wachtwoord == 'geheim':
    print(f'Welkom {naam} je bent ingelogd')
else:
    print('Je wachtwoord is niet correct')

exit()

def som(getal1, getal2):
    return getal1 + getal2

def verschil(getal1, getal2):
    return getal1 - getal2

def product(getal1, getal2):
    return getal1 * getal2

def quotient(getal1, getal2):
    return getal1 / getal2

def macht(getal1, getal2):
    return getal1 ** getal2

def wortel(getal1):
    return getal1 ** 0.5

def kwadraat(getal1):
    return getal1 ** 2

def kubus(getal1):
    return getal1 ** 3

def faculteit(getal1):
    return 1 if getal1 == 0 else getal1 * faculteit(getal1 - 1)

def modulo(getal1, getal2):
    return getal1 % getal2

def gemiddelde(getal1, getal2):
    return (getal1 + getal2) / 2

def maximum(getal1, getal2):
    return getal1 if getal1 > getal2 else getal2

def minimum(getal1, getal2):
    return getal1 if getal1 < getal2 else getal2

def absolute(getal1):
    return abs(getal1)

def afronden(getal1):
    return round(getal1)

def afronden_naar_boven(getal1):
    return math.ceil(getal1)

def afronden_naar_beneden(getal1):
    return math.floor(getal1)

def sinus(getal1):
    return math.sin(getal1)

def cosinus(getal1):
    return math.cos(getal1)

def tangens(getal1):
    return math.tan(getal1)

def arcsinus(getal1):
    return math.asin(getal1)

def arccosinus(getal1):
    return math.acos(getal1)

def arctangens(getal1):
    return math.atan(getal1)

def logaritme(getal1):
    return math.log(getal1)

print(som(getal1, getal2))
print(verschil(getal1, getal2))
print(product(getal1, getal2))
print(quotient(getal1, getal2))
print(macht(getal1, getal2))
print(wortel(getal1))
print(kwadraat(getal1))