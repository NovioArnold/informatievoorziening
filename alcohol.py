naam = input('Wat is je naam? ')
try:
    leeftijd = int(input('Wat is je leeftijd? '))
except ValueError:
    print('Voer een getal in')
    exit()

if leeftijd < 18:
    (print(f'Hallo {naam}, je bent nog geen 18 jaar, je mag nog geen alcohol drinken'))

else:
    (print(f'Hallo {naam}, je bent al 18 jaar, je mag alcohol drinken'))

exit()