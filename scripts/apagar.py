import socket
import subprocess

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

sc, addr = s.accept()

def apagar(seg):
    # Apagar
    subprocess.call("shutdown -s -f -t %d" % seg)

def reiniciar(seg):
    # Reiniciar
    subprocess.call("shutdown -r -f -t %d" % seg)

def abortar():
    # Abortar
    subprocess.call("shutdown -a")

while True:
    recibido = sc.recv(1024)
    str = recibido.split()
    if str[0] == "salir":
        break
    elif str[0] == "apagar":
        apagar((int(str[1]))*60)
        sc.send("Se a programado: Apagar")
        print("Se a programado: Apagar")
    elif str[0] == "reiniciar":
        reiniciar((int(str[1]))*60)
        sc.send("Se a programado: Reiniciar")
        print("Se a programado: Reiniciar")
    elif str[0] == "abortar":
        abortar()
        sc.send("Se a dado la orden de abortar")
        print("Abortado")

#Fin    
print("Programa finalizado")
raw_input()

sc.close()
s.close()