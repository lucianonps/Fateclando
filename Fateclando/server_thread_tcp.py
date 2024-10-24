import socket
import rsa
from threading import Thread

def conexao(con, cli):
    try:
        while True:
            msg = con.recv(1024)
            if not msg: 
                break

            # Carrega a chave privada
            try:
                with open(r'C:\Users\Samsung\Criptografia\luluPri.txt', 'rb') as arq:
                    chave_privada = arq.read()

                # Decodifica a chave no formato correto
                pri = rsa.PrivateKey.load_pkcs1(chave_privada, format='PEM')

                # Decifra a mensagem recebida
                try:
                    mensagem_decifrada = rsa.decrypt(msg, pri)
                    print('Mensagem decifrada com sucesso:')
                    print(mensagem_decifrada.decode('utf-8'))
                except rsa.DecryptionError:
                    print('Falha ao decifrar a mensagem.')
            except FileNotFoundError:
                print('Arquivo de chave não encontrado. Verifique o caminho.')
            except Exception as e:
                print(f'Erro ao carregar a chave privada: {e}')
    except Exception as e:
        print(f'Erro na conexão com o cliente {cli}: {e}')
    finally:
        print('Finalizando conexão com o cliente', cli)
        con.close()

# Endereço IP e Porta do Servidor
HOST = ''  # Aceitar conexões de qualquer endereço
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(5)  # Escuta até 5 conexões simultâneas

print('Servidor TCP aguardando conexões...')
try:
    while True:
        con, cliente = tcp.accept()
        print('Conectado por', cliente)
        t = Thread(target=conexao, args=(con, cliente,))
        t.start()
except KeyboardInterrupt:
    print('\nServidor encerrado pelo usuário.')
finally:
    tcp.close()
