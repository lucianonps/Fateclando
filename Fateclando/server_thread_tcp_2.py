#Servidor TCP
import socket
import rsa

from threading import Thread

def conexao(con,cli):
    while True:
        msg = con.recv(1024)
        if not msg: break
        ####

        ##abro o arquivo com a chave
        arq = open('e:\\chaves\\chavePri.txt', 'rb')
        ##carrego a chave
        txt = arq.read()
        arq.close()

        #decodifico para o formato expoente e modulo
        pri = rsa.PrivateKey.load_pkcs1(txt, format='PEM')

        #decifro a msg
        msg = rsa.decrypt(msg,pri)

        print('Mensagem decifrada com sucesso ')

        ####
        print (msg)
    print ('Finalizando conexao do cliente', cli)
    con.close() 

# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t = Thread(target=conexao, args=(con,cliente,))
    t.start()
