import socket

s = socket.socket()
s.connect(("localhost", 9999))

    
op=0
while op!=4:
    print("\n\tApagado Automatico")
    print("1: Apagar")
    print("2: Reiniciar")
    print("3: Abortar")
    print("4: Salir")
    while True:
        try:
            op = int(input("> "))
            break
        except ValueError:
            print("Opcion no valida, verifique..")
    if op==1:
        print("Orden de apagado, ingrese el tiempo en minutos: ")
        while True:
            try:
                time= int(input("> "))
                break
            except ValueError:
                print("Formato no valido, ingrese el tiempo en minutos: ")
        print("Apagado en "+ str(time)+ " minutos")
        cmd = "apagar "+ str(time)
        s.send(cmd)
        rec=s.recv(1024)
        print(rec)
    elif op==2:
        print("\n")
        print("Orden de reiniciar, ingrese el tiempo en minutos: ")
        while True:
            try:
                time= int(raw_input("> "))
                break
            except ValueError:
                print("Formato no valido, ingrese el tiempo en minutos: ")
        print("\n")
        print("Reinicio en "+ str(time)+ " minutos")
        cmd= "reiniciar "+str(time)
        s.send(cmd)
        rec=s.recv(1024)
        print(rec)
    elif op==3:
        print("\n")
        print("Orden abortar apagado o reinicio")
        cmd= "abortar 0"
        s.send(cmd)
        rec=s.recv(1024)
        print(rec)
    elif op==4:
        print("\n")
        cmd= "salir 0"
        s.send(cmd)
        break
    else:
        print("\n")
        print("Opcion no valida, verifique..\n")

print("Programa finalizado")
raw_input()
s.close()