import random

def raadspel():
    random_getal = random.randint(1, 100)
    pogingen = 0

    print("Welkom bij het getal raadspel!")
    print("Ik heb een getal tussen 1 en 100 gekozen. Kun jij het raden?")

    while True:
        try:
            gok = int(input("Voer je gok in: "))
            pogingen += 1

            if gok < random_getal:
                print("Te laag! Probeer het opnieuw.")
            elif gok > random_getal:
                print("Te hoog! Probeer het opnieuw.")
            else:
                print(f"Gefeliciteerd! Je hebt het juiste getal {random_getal} geraden in {pogingen} pogingen.")
                break
        except ValueError:
            print("Voer een geldig getal in.")

raadspel()