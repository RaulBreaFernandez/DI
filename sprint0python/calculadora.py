from operaciones import addition, subtraction, multiplication, division

def main():

    op = 0
    num1 = 0
    num2 = 0
    result = 0
    seguir = "S"

    while seguir == "S":

        print("Introduce 2 números para operar con ellos")
        num1 = int(input("Primer número:"))
        num2 = int(input("Segundo número:"))

        print("¿Qué operación quieres hacer?")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicación")
        print("4 - División")
        op = int(input("Elige una opción del 1 al 4\n"))

        #Comprobación de la operación que quiere hacer el/la usuari@

        if op == 1:

            result = addition(num1, num2)

        elif op == 2:

            result = subtraction(num1, num2)

        elif op == 3:

            result = multiplication(num1, num2)

        elif op == 4:

            result = division(num1, num2)

        else:
            
            print("Elige una opción de las que están disponibles")
            

        #Damos el resultado
        print(result)

        #Preguntamos si quiere continuar haciendo operaciones
        seguir = input("¿Quieres seguir jugando? (S para SÍ, N para NO)").upper()

        while seguir != "S" and seguir != "N":

            print("Has elegido una opción incorrecta. Elige entre SÍ o NO")
            
            seguir = input("¿Quieres seguir jugando? (S para SÍ, N para NO)")

main() 