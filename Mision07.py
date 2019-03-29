#Autor:Karla Ximena Rueda Ruiz
#Este programa calcula divisores y en una serie de números encuentra al número mayor.

def probarDivisiones(dividendo, divisor):
    con=1
    termina=False
    lista=[]
    while not termina:
        if(divisor*con<=dividendo):
            lista.append(con)
            con=con+1
        else:
            termina=True
    residuo=dividendo-(divisor*max(lista))
    print(dividendo," / ",divisor," = ",max(lista), ", sobra ",residuo)
    main()




def encuentraMayor():

    print("Teclea una serie de numeros para encontrar el mayor.")

    listaDeNum=[]

    valorAsignado=int(input("Teclea un número [-1 para salir]: "))

    if valorAsignado!=-1:

        while valorAsignado!=-1:

            listaDeNum.append(valorAsignado)

            valorAsignado = int(input("Teclea un número [-1 para salir]: "))

        print("El numero mayor es: ",max(listaDeNum))

        main()

    else:

        print("No hay valor mayor")

        main()

def main():

    print('''Mision 07.Ciclos while

Autor: Karla Ximena Rueda Ruiz
Matricula:A01745943

1. Calcular divisores 

2. Encontrar el mayor

3. Salir''')

    opcionUsuario=int(input("Teclea tu opcion: "))

    if opcionUsuario==1:

        dividendo = int(input('ingresa el dividendo: '))
        divisor = int(input('ingresa el divisor: '))

        probarDivisiones(dividendo, divisor)


    elif opcionUsuario==2:

        encuentraMayor()

    elif opcionUsuario==3:

        print("Gracias por usar este programa, regresa pronto")

    else:

        print("ERROR, teclea 1,2 o 3")


main()
