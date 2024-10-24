#Cliente TCP
import socket
import rsa

# Endereco IP do Servidor
SERVER = '192.168.5.91'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input().encode('utf-8')
while msg != '\x18':
    ####

    ##abro o arquivo com a chave
    arq = open('e:\chaves\chave2Pub.txt','rb')
    ##carrego a chave
    txt = arq.read()
    arq.close()

    #decodifico para o formato expoente e modulo
    pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

    #cifro a msg
    msg = rsa.encrypt(msg,pub)

    print('Mensagem cifrada com sucesso')

    ####
    tcp.send (msg)
    msg = input()
tcp.close()
