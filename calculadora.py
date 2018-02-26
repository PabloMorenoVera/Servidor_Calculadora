#!/usr/bin/python3

#Programa para simular una calculadora
import sys

def calculate(op1, operacion, op2):
    try:
        if operacion == 'suma':
            return(str(int(op1)+int(op2)))
        elif operacion == 'multiplica':
            return(str(int(op1)*int(op2)))
        elif operacion == 'divide':
            return(str(int(op1)/int(op2)))
        elif operacion == 'resta':
            return(str(int(op1)-int(op2)))
        else:
            return('Nombre de la funcion incorrecto')
    except ZeroDivisionError:
        return('Division entre 0')

if __name__ == '__main__':
    try:
        if len(sys.argv) == 4:
            if sys.argv[1] == 'suma':
                print(int(sys.argv[2])+int(sys.argv[3]))
            elif sys.argv[1] == 'multiplica':
                print(int(sys.argv[2])*int(sys.argv[3]))
            elif sys.argv[1] == 'divide':
                print(int(sys.argv[2])/int(sys.argv[3]))
            elif sys.argv[1] == 'resta':
                print(int(sys.argv[2])-int(sys.argv[3]))
            else:
                print('Función introducida errónea. Introduce : "+", "-", "\*", "/"')
        else:
            print('Número de argumentos incorrecto. Por favor introuzca: Nombre_Progama Función Número Número')

    except ValueError:
        print('Números mal introducidos. Por favor introduzca: Nombre_Progama Función Número Número')
