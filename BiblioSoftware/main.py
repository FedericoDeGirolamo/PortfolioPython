Libri = {}

def aggiungi_libro(titolo, copie):
    if copie <= 0:
        print("Errore, inserire un numero di copie positivo")
        return
    if (titolo in Libri):
        Libri[titolo] += copie
    else:
        Libri[titolo] = copie
    print("Il libro è stato aggiunto al database")

def rimuovi_libro(titolo):
    if (titolo in Libri):
        Libri.pop(titolo)
    else:
        print("Errore, il libro non è in catalogo")

def verifica_disponibilita(titolo):
    if (titolo in Libri):
        if (Libri[titolo] > 0):
            return True
        else:
            return False
    else:
        return False

def prendi_in_prestito(titolo):
    if (titolo in Libri):
        if (Libri[titolo] > 0):
            Libri[titolo] -= 1
            print("Prestito effettuato con successo")
        else:
            print("Non ci sono copie disponibili")
    else:
        print("Il libro non è in catalogo")

def statistiche_biblioteca():
    titoli = 0
    copie = 0
    for k, v in Libri.items():
        copie += v
    titoli = len(Libri)
    if (titoli > 0):
        media = copie / titoli
    else:
        media = 0
    stats = {"totale_libri": titoli, "copie_totali": copie, "media_copie": media}
    return stats

def visualizza_libri():
    if (len(Libri) == 0):
        print("Non sono presenti libri nell'archivio")
    else:
        for k, v in Libri.items():
            print("Titolo libro:", k, "Numero di copie:", v)

def restaurare_libro(titolo, copie):
    if titolo in Libri:
        Libri[titolo] += copie
        print("Copie restaurate con successo")
    else:
        print("Errore, impossibile restaurare: il libro non è in archivio")


# SOFTWARE:

while True:
    azione = input("Cosa vuoi fare? (aggiungi / rimuovi / verifica disponibilità / prestito / statistiche / visualizza / restaura / esci) ")
    if (azione == "esci"):
        print("Programma in chiusura")
        break
    elif (azione == "aggiungi"):
        titolo_nuovo = input("Inserire il titolo del libro ").title()
        numero_copie_nuovo = int(input("Inserire il numero di copie "))
        aggiungi_libro(titolo_nuovo, numero_copie_nuovo)
    elif (azione == "rimuovi"):
        titolo_da_rimuovere = input("Inserire il titolo da rimuovere ").title()
        rimuovi_libro(titolo_da_rimuovere)
    elif (azione == "verifica disponibilità"):
        titolo_da_verificare = input("Inserisci il titolo per cui verificare la disponibilità ").title()
        disponibile = verifica_disponibilita(titolo_da_verificare)
        if disponibile:
            print("Il libro è disponibile!")
        else:
            print("Il libro non è disponibile o non è in catalogo")
    elif (azione == "prestito"):
        titolo_libro_prestato = input("Inserisci il titolo del libro preso in prestito ").title()
        prendi_in_prestito(titolo_libro_prestato)
    elif (azione == "statistiche"):
        dati = statistiche_biblioteca()
        print("Ecco una panoramica delle statistiche della biblioteca")
        print(dati)
    elif (azione == "visualizza"):
        visualizza_libri()
    elif (azione == "restaura"):
        titolo_restaurato = input("Inserisci il titolo del libro restaurato ").title()
        copie_restaurate = int(input("Inserisci il numero di copie restaurate "))
        restaurare_libro(titolo_restaurato, copie_restaurate)
    else:
        print("Comando non esistente, riscrivilo correttamente!")
