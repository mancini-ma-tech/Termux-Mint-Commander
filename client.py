import socket
import sys

# Configurazione di Rete
SERVER_IP = 'INSERISCI_QUI_IL_TUO_IP'
PORT = 9999


def invia_comando(comando_da_inviare):
    """Stabilisce la connessione e invia il pacchetto dati al server."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, PORT))
        client.send(comando_da_inviare.encode('utf-8'))
        client.close()
        print(
            f"[+] Trasmesso: Comando '{comando_da_inviare}' inviato con successo.")
    except Exception as e:
        print(f"[-] Errore critico: Impossibile stabilire la connessione col server.")
        print(f"    Dettaglio eccezione: {e}")


if __name__ == "__main__":
    print("=============================================")
    print(" INTERFACCIA DI CONTROLLO REMOTO (CLIENT)")
    print("=============================================")

    while True:
        print("\nParametri disponibili:")
        print("1. [Audio] Modifica stato volume (Mute/Unmute)")
        print("2. [Sicurezza] Blocca sessione di lavoro")
        print("3. [Test] Trasmetti notifica di sistema")
        print("4. [Alimentazione] Inizia sequenza di spegnimento (Timer 60s)")
        print("5. [Alimentazione] Annulla spegnimento in corso")
        print("6. [Interazione] Trasmissione Text-to-Speech (Sintesi Vocale)")
        print("0. Termina esecuzione client")

        scelta = input("\nInserire il codice dell'operazione desiderata: ")

        if scelta == "1":
            invia_comando("MUTA")
        elif scelta == "2":
            invia_comando("BLOCCO")
        elif scelta == "3":
            invia_comando("NOTIFICA")
        elif scelta == "4":
            print("[!] Attenzione: Spegnimento del server programmato tra 60 secondi.")
            invia_comando("SPEGNI")
        elif scelta == "5":
            invia_comando("ANNULLA_SPEGNI")
        elif scelta == "6":
            frase = input("Inserisci la frase da far pronunciare al server: ")
            # Uniamo il prefisso PARLA: con la frase inserita
            invia_comando(f"PARLA:{frase}")
        elif scelta == "0":
            print("[*] Disconnessione effettuata. Chiusura programma.")
            sys.exit(0)
        else:
            print("[-] Input non valido. Selezionare un indice compreso tra 0 e 6.")
