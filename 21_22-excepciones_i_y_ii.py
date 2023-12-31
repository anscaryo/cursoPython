'''
    Error de tiempo de ejecución. La sintaxi es correcta pero 
    durante la ejecución ocurre algo inesperado.
'''

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0.")
        return "Operación erronea."
    

while True:

    try:
        op1 = int(input("Introduce el primer numero: "))
        op2 = int(input("Introduce el segundo numero: "))
        break
    except ValueError:
        print("valor no valido")
    

operacion = input("Introduce la operación a realizar: ( suma, resta, multiplica, divide) ").lower()

if operacion == "suma":
    print(suma(op1,op2))

elif operacion == "resta":
    print(resta(op1,op2))

elif operacion == "multipica":
    print(multiplica(op1,op2))

elif operacion == "divide":
    print(divide(op1,op2))

else:
    print("Operación no contemplada.")

print("Operación ejecutada, Continua la ejecución del programa.")