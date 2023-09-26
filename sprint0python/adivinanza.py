def verifyAnswer(userAnswer) :

    #método para comprobar la respuesta

    realAnswer = "a"

    if(userAnswer.lower() == realAnswer) :

        print("Has acertado")
    
    else:

       print("Has fallado")
    
def showRiddle():    

    #método para mostrar la adivinanza, sus respuestas y comprobación de que 
    #se introduce una respuesta válida 

    answer = ""

    while answer != "a" and answer != "b" and answer != "c":

        print("Aunque tengo cuatro patas, yo nunca puedo comer, tengo la comida encima y no la puedo comer")
        print("a) La mesa")
        print("b) La silla")
        print("c) La cama")

        answer = input("Adivina la respuesta correcta\n")

        if answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c":

            print("Escoge una de las respuestas disponibles")

        else:  
            
            verifyAnswer(answer) 

def main():

    showRiddle()


main()


   