#Importamos random para que las adivinanzas aparezcan de manera aleatoria
import random

#Lista del 1 al 3 para las adivinanzas
number = list(range(1, 4))

def showRiddle():    

    #método para mostrar la adivinanza, sus respuestas y comprobación de que 
    #se introduce una respuesta válida 

    answer1 = "" 
    answer2 = ""  
    answer3 = ""
    score = 0

    #Sacamos 2 números aleatorios de la lista
    sample = random.sample(number, 2)

    if sample[0] == 1 or sample[1] == 1:
        
        while answer1 != "a" and answer1 != "b" and answer1 != "c":

            print("Aunque tengo cuatro patas, yo nunca puedo comer, tengo la comida encima y no la puedo comer")
            print("a) La mesa")
            print("b) La silla")
            print("c) La cama")

            answer1 = input("Adivina la respuesta correcta\n")

            if answer1.lower() != "a" and answer1.lower() != "b" and answer1.lower() != "c":

                print("Escoge una de las respuestas disponibles")

            else:  
                
                if(answer1) == "a":

                    print("Has acertado")
                    score += 10

                else:

                    print("Has fallado")    
                    score -= 5

    if sample[0] == 2 or sample[1] == 2:

        while answer2 != "a" and answer2 != "b" and answer2 != "c":

            print("Salta y salta, y la colita le falta.")
            print("a) El conejo")
            print("b) La rana")
            print("c) El caballo")

            answer2 = input("Adivina la respuesta correcta\n")

            if answer2.lower() != "a" and answer2.lower() != "b" and answer2.lower() != "c":

                print("Escoge una de las respuestas disponibles")

            else:  
                
                if answer2 == "b":

                    print("Has acertado")
                    score += 10

                else:

                    print("Has fallado") 
                    score -= 5 
    

    if sample[0] == 3 or sample[1] == 3:

        while answer3 != "a" and answer3 != "b" and answer3 != "c":

            print("Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.")
            print("a) La manzana")
            print("b) La naranja")
            print("c) La pera")

            answer3 = input("Adivina la respuesta correcta\n")

            if answer3.lower() != "a" and answer3.lower() != "b" and answer3.lower() != "c":

                print("Escoge una de las respuestas disponibles")

            else:  
                
                if answer3 == "c":

                    print("Has acertado")
                    score += 10

                else:

                    print("Has fallado")
                    score -= 5    


    #comprobamos la puntuación total del/la participante
    
    if(score < 0):

        score = 0 

    if(score == 0):

        print("Tu puntuación es de "+str(score)+" puntos! No puedes ser tan mal@ ni queriendo")

    elif(score == 5):

        print("Tu puntuación es de "+str(score)+" puntos! Sé que puedes hacerlo mejor")
        
    elif(score == 20):

        print("Tu puntuación es de "+str(score)+" puntos! Perfecto!")     

def main():

    showRiddle()


main()


   