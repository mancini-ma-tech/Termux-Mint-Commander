import socket

# 1. Il numero di telefono del tuo PC Mint
# (Attenzione: mantieni le virgolette singole intorno ai numeri!)
SERVER_IP = '192.168.1.6' 
PORT = 9999

def invia_comando(comando_da_inviare):
    try:
        # 2. Prendiamo il telefono in mano (creiamo il socket client)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 3. Componiamo il numero e chiamiamo il PC
        client.connect((SERVER_IP, PORT))
        
        # 4. Parliamo! (Inviamo il messaggio traducendolo in byte)
        client.send(comando_da_inviare.encode('utf-8'))
        
        # 5. Riagganciamo per chiudere la comunicazione pulita
        client.close()
        
        print(f"✅ Successo! Comando '{comando_da_inviare}' recapitato al quartier generale.")
        
    except Exception as e:
        print(f"❌ Disastro! Impossibile connettersi al PC. Errore: {e}")
        print("💡 Controlla che l'IP sia corretto e che il server sia acceso.")

if __name__ == "__main__":
    print("📱 Avvio del Telecomando Aria...")
    # 6. Simuliamo la pressione di un tasto sul telecomando
    invia_comando("NOTIFICA")