import socket
import subprocess

# Configurazione di Rete
HOST = '0.0.0.0'
PORT = 9999


def esegui_azione(comando):
    """Elabora e converte le stringhe di comando in esecuzioni di sistema."""
    print(f"[Sistema] Ricezione direttiva: {comando}")

    if comando == "NOTIFICA":
        subprocess.run(["notify-send", "Sistema Remoto",
                       "Connessione stabilita con successo."])
        print("[+] Esecuzione: Notifica inviata a schermo.\n")

    elif comando == "MUTA":
        subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"])
        print("[+] Esecuzione: Stato del dispositivo audio modificato.\n")

    elif comando == "BLOCCO":
        subprocess.run(["cinnamon-screensaver-command", "--lock"])
        print("[+] Esecuzione: Sessione utente bloccata.\n")

    elif comando == "SPEGNI":
        subprocess.run(
            ["shutdown", "+1", "Spegnimento remoto programmato tra 60 secondi."])
        print("[!] Allerta: Procedura di spegnimento programmato avviata.\n")

    elif comando == "ANNULLA_SPEGNI":
        subprocess.run(["shutdown", "-c"])
        subprocess.run(["notify-send", "Sistema Remoto",
                       "Spegnimento annullato dall'amministratore."])
        print("[-] Operazione: Procedura di spegnimento interrotta.\n")

    else:
        print("[-] Errore: Direttiva non riconosciuta dal sistema.\n")


def avvia_server():
    """Inizializza il socket e mantiene il demone in ascolto."""
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
