import socket

# 1. Configuriamo la "frequenza radio"
HOST = '0.0.0.0'
PORT = 9999

def avvia_server():
    # 2. Creiamo la ricetrasmittente (il socket)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 3. Accendiamo e sintonizziamo
    server.bind((HOST, PORT))
    
    # 4. Mettiamoci in ascolto
    server.listen(1)

    print("=========================================")
    print(f"📡 Zietta Aria in ascolto sul fisso...")
    print(f"🎯 Radar acceso sulla porta: {PORT}")
    print("⏳ Aspetto il segnale...")
    print("=========================================\n")

    # --- ECCO LA NOVITÀ ---
    while True:
        # 5. Rispondiamo alla "chiamata" in arrivo
        client, indirizzo = server.accept()
        print(f"🚨 BOOM! Qualcuno ha bussato dall'indirizzo IP: {indirizzo}")

        # 6. Ascoltiamo il messaggio (pacchetto dati max 1024 byte) e lo traduciamo in testo
        messaggio = client.recv(1024).decode('utf-8')
        print(f"📩 Comando ricevuto: {messaggio}")

        # 7. Riagganciamo per liberare la linea
        client.close()
        print("📞 Linea chiusa. Torno a fare la guardia...\n")

if __name__ == "__main__":
    avvia_server()