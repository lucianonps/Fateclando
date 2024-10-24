import socket
import rsa

# Endereço IP do Servidor
SERVER = '192.168.137.229'
# Porta que o Servidor está escutando
PORT = 5002

# Cria o socket TCP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conecta ao servidor
    dest = (SERVER, PORT)
    tcp.connect(dest)
    print('Conectado ao servidor. Para sair use CTRL+X\n')

    while True:
        msg = input('Digite a mensagem a ser enviada (CTRL+X para sair): ').strip().encode('utf-8')
        
        # Verifica se o usuário deseja sair
        if msg == '\x18':  # CTRL+X
            print('Saindo do cliente...')
            break
        
        # Carrega a chave pública
        try:
            with open(r'C:\Users\Samsung\Criptografia\chavestestePub.txt', 'rb') as arq:
                chave_pub = arq.read()

            # Decodifica a chave no formato correto
            pub = rsa.PublicKey.load_pkcs1(chave_pub, format='PEM')

            # Cifra a mensagem
            msg_cifrada = rsa.encrypt(msg, pub)
            print('Mensagem cifrada com sucesso')

            # Envia a mensagem cifrada para o servidor
            tcp.send(msg_cifrada)
            print('Mensagem enviada com sucesso.')
        
        except FileNotFoundError:
            print('Erro: Arquivo de chave pública não encontrado. Verifique o caminho.')
            break
        except rsa.DecryptionError:
            print('Erro: Falha ao cifrar a mensagem.')
            break
        except Exception as e:
            print(f'Erro inesperado: {e}')
            break

except ConnectionRefusedError:
    print('Erro: O servidor está indisponível. Verifique se o endereço IP e a porta estão corretos.')
except Exception as e:
    print(f'Erro inesperado ao conectar: {e}')
finally:
    tcp.close()
    print('Conexão encerrada.')
