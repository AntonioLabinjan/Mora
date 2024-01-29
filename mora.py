import random

def igra_protiv_racunala():
    print("Dobrodošli u tradicionalnu talijansku igru koju su Istrijani prisvojili!")

    bodovi_igrac = 0
    bodovi_racunalo = 0

    while True:
        try:
            picked = int(input("Odaberite broj (1-10): "))
            thrown = int(input("Unesite broj prstiju koje ćete pokazati (1-5): "))
        except ValueError:
            print("Unesite ispravan broj.")
            continue
        if thrown >= picked:
            print("Broj prstiju koje pokazujete mora biti manji od odabranog broja.")
            continue

        while True:
            comp_picked = random.randint(1, 10)
            comp_thrown = random.randint(1, 5)

            if comp_thrown < comp_picked:
                break

        print(f"Računalo odabire broj {comp_picked} i pokazuje {comp_thrown} prstiju.")
        print(f"Igrač odabire broj {picked} i pokazuje {thrown} prstiju.")

        sum = thrown + comp_thrown

        print(f"Zbroj prstiju: {sum}")

        if comp_picked == picked == sum:
            print("Igrač i računalo pogodili su zbroj! Oboje osvajaju po bod.")
            bodovi_igrac += 1
            bodovi_racunalo += 1
        elif comp_picked == sum:
            print("Računalo osvaja bod!")
            bodovi_racunalo += 1
        elif picked == sum:
            print("Vi osvajate bod!")
            bodovi_igrac += 1
        else:
            print('Nitko nije osvojio bod')

        print(f"Vaši bodovi: {bodovi_igrac}, Bodovi računala: {bodovi_racunalo}")

        ponovno = input("Želite li ponovno igrati? (da/ne): ")
        if ponovno.lower() != 'da':
            break

    print(f"Konačan rezultat - Vaši bodovi: {bodovi_igrac}, Bodovi računala: {bodovi_racunalo}")

if __name__ == "__main__":
    igra_protiv_racunala()
