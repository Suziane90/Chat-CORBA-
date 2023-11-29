import threading
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 59000))
# fornecer o endereço IP do servidor e a porta correta durante a execução do cliente
def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "apelido?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Erro!')
            client.close()
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

alias = input('Escolha um apelido >>> ')
client.send(alias.encode('utf-8'))

print("Conexão estabelecida com sucesso! Você pode começar a conversar.")

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()