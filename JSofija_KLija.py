import time

# Funkcija, kas uzdod jautājumu un pārbauda atbildi
def uzdot_jautajumu(jautajums, atbildes_varianti, pareiza_atbilde):
    """Šī funkcija uzdod jautājumu un pārbauda atbildi."""
    print(jautajums)
    
    # Izdrukājam atbilžu variantus
    for i, atbilde in enumerate(atbildes_varianti, 1):
        print(f"{i}. {atbilde}")

    # Pieprasām lietotāja izvēli
    while True:
        try:
            lietotaja_atbilde = int(input("Ievadi atbildes numuru (1-4): "))
            if 1 <= lietotaja_atbilde <= 4:
                break
            else:
                print("Lūdzu ievadi derīgu atbildes numuru no 1 līdz 4.")
        except ValueError:
            print("Lūdzu ievadi skaitli no 1 līdz 4.")
    
    # Pārbaudām, vai lietotāja izvēlētā atbilde ir pareiza
    if lietotaja_atbilde == pareiza_atbilde:
        print("Pareizi! 👍\n")
        return 1  # Ja atbilde pareiza, atgriežam 1 punktu
    else:
        print(f"Nepareizi! Pareizā atbilde bija: {atbildes_varianti[pareiza_atbilde - 1]}\n")
        return 0  # Ja atbilde nepareiza, atgriežam 0 punktu

# Funkcija, kas veic spēles galveno loģiku
def spelot_viktorinu():
    """Galvenā spēles funkcija, kas organizē viktorīnu un skaita punktus."""
    jautajumi = [
        {
            "jautajums": "Kāds ir Latvijas galvaspilsētas nosaukums?",
            "atbildes": ["Rīga", "Liepāja", "Jelgava", "Daugavpils"],
            "pareiza_atbilde": 1
        },
        {
            "jautajums": "Kāds ir lielākais dzīvnieks uz Zemes?",
            "atbildes": ["Zilonis", "Baltais lācis", "Zirgs", "Zilais valis"],
            "pareiza_atbilde": 4
        },
        {
            "jautajums": "Kurā gadā sākās Pirmais pasaules karš?",
            "atbildes": ["1914", "1900", "1939", "1912"],
            "pareiza_atbilde": 1
        },
        {
            "jautajums": "Kāds ir cilvēka ķermeņa lielākais orgāns?",
            "atbildes": ["Plaušas", "Acu tīklenes", "Aknas", "Āda"],
            "pareiza_atbilde": 4
        },
        {
            "jautajums": "Kurā kontinentā atrodas Āfrikas tuksnesis Sahāra?",
            "atbildes": ["Eirāzija", "Āfrika", "Ziemeļamerika", "Okeānija"],
            "pareiza_atbilde": 2
        }
    ]

    print("Laipni lūdzam viktorīnā!\n")
    time.sleep(1)  # Pārtraukums, lai spēlētājs varētu sagatavoties

    punkti = 0  # Punktu skaitītājs
    
    # Iterējam cauri visiem jautājumiem
    for jautajums in jautajumi:
        punktu_pievienosana = uzdot_jautajumu(jautajums["jautajums"], jautajums["atbildes"], jautajums["pareiza_atbilde"])
        punkti += punktu_pievienosana  # Pievienojam punktus, ja atbilde ir pareiza
    
    # Spēles noslēgums
    print(f"Viktorīnas beigas! Tu ieguvi {punkti} no {len(jautajumi)} punktiem.\n")
    if punkti == len(jautajumi):
        print("Apsveicam! Tu atbildēji pareizi uz visiem jautājumiem!")
    elif punkti > len(jautajumi) // 2:
        print("Lieliski! Tu esi zinātkārs spēlētājs!")
    else:
        print("Lieliski mēģināts! Mēģini vēlreiz un uzlabot savu rezultātu.")

# Funkcija, kas piedāvā spēlēt vēlreiz
def jautat_par_speli():
    """Funkcija piedāvā spēlēt spēli vēlreiz."""
    while True:
        atbilde = input("Vai vēlies spēlēt vēlreiz? (jā/nē): ").strip().lower()
        if atbilde == "jā":
            return True  # Ja atbilde ir "jā", spēle turpinās
        elif atbilde == "nē":
            print("Paldies par spēlēšanu! Atā!")
            return False  # Ja atbilde ir "nē", spēle beidzas
        else:
            print("Lūdzu, ievadi 'jā' vai 'nē'.")

# Galvenā funkcija, kas uzsāk spēles loģiku
def galvena_funkcija():
    """Galvenā funkcija, kas uzsāk spēli un organizē spēlētāja izvēli spēlēt vēlreiz."""
    while True:
        spelot_viktorinu()  # Sāk spēli
        if not jautat_par_speli():  # Ja lietotājs nevēlas spēlēt vēlreiz, beidzam spēli
            break

# Palaižam galveno funkciju
if __name__ == "__main__":
    galvena_funkcija()
