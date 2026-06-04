import socket
import subprocess  # La nuova libreria per controllare il sistema operativo!

HOST = '0.0.0.0'
PORT = 9999

def esegui_azione(comando):
    print(f"⚙️ Elaborazione del comando: {comando}")
    
    if comando == "NOTIFICA":
        subprocess.run(["notify-send", "📱 Telecomando S25", "Messaggio recapitato!"])
        print("📣 Notifica sparata a schermo.\n")
        
    elif comando == "MUTA":
        # 'pactl' dice al sistema audio principale (@DEFAULT_SINK@) di fare un toggle (invertire) il mute
        subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"])
        print("🔇 Interruttore audio attivato con successo.\n")
def avvia_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print("=========================================")
    print(f"📡 Aria in ascolto sul fisso...")
    print("⏳ Aspetto ordini dal telefono...")
    print("=========================================\n")

    while True:
        client, indirizzo = server.accept()
        messaggio = client.recv(1024).decode('utf-8')
        
        print(f"🚨 BOOM! Contatto stabilito dall'IP: {indirizzo[0]}")
        
        # Invece di stampare solo il messaggio, lo passiamo alla nuova funzione!
        esegui_azione(messaggio)
        
        client.close()

if __name__ == "__main__":
    avvia_server()