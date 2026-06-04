import socket
import subprocess
import os

# Configurazione di Rete
HOST = '0.0.0.0'
PORT = 9999


def esegui_azione(comando):
    """Elabora e converte le stringhe di comando in esecuzioni di sistema."""
    print(f"[Sistema] Ricezione direttiva: {comando}")

    # === MEDIA E INTERAZIONE ===
    if comando == "NOTIFICA":
        subprocess.run(["notify-send", "Sistema Remoto",
                       "Connessione stabilita con successo."])
        print("[+] Esecuzione: Notifica inviata a schermo.\n")

    elif comando == "MUTA":
        subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"])
        print("[+] Esecuzione: Stato del dispositivo audio modificato.\n")

    elif comando.startswith("PARLA:"):
        frase_da_dire = comando.split(":", 1)[1]
        subprocess.run(["spd-say", "-l", "it", "-t", "female1", frase_da_dire])
        print(f"[+] Audio: Sintesi vocale eseguita.\n")

    elif comando.startswith("APRI:"):
        url = comando.split(":", 1)[1]
        subprocess.run(["xdg-open", url])
        print(f"[+] Rete: Link aperto nel browser predefinito.\n")

    # === ALIMENTAZIONE E SICUREZZA BASE ===
    elif comando == "BLOCCO":
        subprocess.run(["cinnamon-screensaver-command", "--lock"])
        print("[+] Sicurezza: Sessione utente bloccata.\n")

    elif comando == "SPEGNI":
        subprocess.run(
            ["shutdown", "+1", "Spegnimento remoto tra 60 secondi."])
        print("[!] Allerta: Spegnimento programmato avviato.\n")

    elif comando == "ANNULLA_SPEGNI":
        subprocess.run(["shutdown", "-c"])
        subprocess.run(["notify-send", "Sistema Remoto",
                       "Spegnimento annullato."])
        print("[-] Operazione: Spegnimento interrotto.\n")

    # === SPIONAGGIO E SICUREZZA AVANZATA ===
    elif comando == "FOTO":
        # Scatta una foto silenziosa e la salva nella cartella Home
        percorso_foto = os.path.expanduser("~/intruso_webcam.jpg")
        subprocess.run(["fswebcam", "-r", "1280x720",
                       "--no-banner", percorso_foto])
        print(
            f"[+] Sicurezza: Fotografia webcam salvata in {percorso_foto}.\n")

    elif comando == "SCREENSHOT":
        percorso_screen = os.path.expanduser("~/screenshot_remoto.png")
        subprocess.run(["gnome-screenshot", "-f", percorso_screen])
        print(f"[+] Sicurezza: Screenshot salvato in {percorso_screen}.\n")

    elif comando == "ALLARME":
        # Alza il volume al 100% e lancia un avviso vocale aggressivo
        subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "100%"])
        subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "0"])
        subprocess.run(["spd-say", "-l", "it", "-t", "female1", "-p", "50",
                       "Allarme intruso. Allontanarsi immediatamente dal computer."])
        print("[!] SICUREZZA CRITICA: Allarme sonoro innescato.\n")

    # === CONTROLLO DI SISTEMA E PRODUTTIVITÀ ===
    elif comando.startswith("KILL:"):
        app = comando.split(":", 1)[1]
        subprocess.run(["killall", app])
        print(f"[-] Sistema: Processo '{app}' terminato forzatamente.\n")

    elif comando == "FOCUS":
        # Apre l'editor di testo (xed su Mint) e silenzia le notifiche
        subprocess.run(["gsettings", "set", "org.cinnamon.desktop.notifications",
                       "display-notifications", "false"])
        subprocess.run(["xed"])
        print("[+] Produttività: Modalità Focus e Text Editor avviati.\n")

    else:
        print("[-] Errore: Direttiva non riconosciuta dal sistema.\n")


def avvia_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print("=========================================")
    print(" INIZIALIZZAZIONE SERVER DI CONTROLLO")
    print(f" Demone in ascolto sulla porta: {PORT}")
    print("=========================================\n")

    while True:
        client, indirizzo = server.accept()
        messaggio = client.recv(1024).decode('utf-8')

        print(f"[Rete] Connessione in ingresso dall'IP: {indirizzo[0]}")
        esegui_azione(messaggio)
        client.close()


if __name__ == "__main__":
    avvia_server()
